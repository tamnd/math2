#!/bin/sh
# Build the wiki of tamnd/math2 and publish it to Cloudflare Pages at https://math2.tamnd.com.
#
# Run it from cron on a build server, for example every 5 minutes: */5 * * * * $HOME/math2-deploy/deploy-cloudflare.sh >> $HOME/math2-deploy/deploy.log 2>&1. The server needs git, Go, Node and flock. It fetches main of tamnd/math2 and tamnd/math2-agent, and it does nothing when the two commits are the same as at the last deploy. Use -f to deploy again.
#
# The file $M2_DEPLOY/cloudflare.env must set CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID. Keep it at mode 600.
set -eu

dir=${M2_DEPLOY:-$HOME/math2-deploy}
project=${M2_PAGES_PROJECT:-math2}
url=${M2_SITE_URL:-https://math2.tamnd.com}
# Cloudflare Pages takes at most 20,000 files and 25 MiB for each file in one deployment. The margin leaves room for the files that wrangler adds.
limit=${M2_PAGES_FILES:-19500}
force=${1:-}

mkdir -p "$dir"
exec 9>"$dir/lock"
flock -n 9 || { echo "another deploy is running"; exit 0; }

set -a
. "$dir/cloudflare.env"
set +a

sync() {
	if [ -d "$dir/$1/.git" ]; then
		git -C "$dir/$1" fetch -q --depth 1 origin main
		git -C "$dir/$1" reset -q --hard FETCH_HEAD
	else
		git clone -q --depth 1 "https://github.com/tamnd/$2.git" "$dir/$1"
	fi
	git -C "$dir/$1" rev-parse HEAD
}

content=$(sync content math2)
toolchain=$(sync toolchain math2-agent)
state="$content $toolchain"
if [ "$force" != "-f" ] && [ -f "$dir/deployed" ] && [ "$(cat "$dir/deployed")" = "$state" ]; then
	exit 0
fi

echo "$(date -u +%FT%TZ) deploy math2 $content, math2-agent $toolchain"
(cd "$dir/toolchain" && go build -trimpath -o "$dir/m2" ./cmd/m2)
rm -rf "$dir/site"
"$dir/m2" site build -content "$dir/content" -spec "$dir/toolchain/spec" -out "$dir/site" -url "$url" -commit "$content" -date now
files=$(find "$dir/site" -type f | wc -l)
big=$(find "$dir/site" -type f -size +24M | head -1)
if [ "$files" -gt "$limit" ] || [ -n "$big" ]; then
	echo "the site has $files files (the limit is $limit) or a file over 24 MB ($big). The deploy stops and the last deployment stays."
	exit 1
fi
npx --yes wrangler@4 pages deploy "$dir/site" --project-name "$project" --branch main --commit-hash "$content" --commit-message "math2 $content" --commit-dirty=true
echo "$state" >"$dir/deployed"
