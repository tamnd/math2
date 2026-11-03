#!/bin/sh
# Build the wiki of tamnd/math2 and publish it to Cloudflare Pages at https://math2.tamnd.com.
#
# Run it from cron on a build server, for example every 5 minutes: */5 * * * * $HOME/math2-deploy/deploy-cloudflare.sh >> $HOME/math2-deploy/deploy.log 2>&1. The server needs git, Go, Node, Python 3 and flock. It fetches main of tamnd/math2 with its history, and main of tamnd/math2-agent and tamnd/wikipedia-math, and it does nothing when the three commits are the same as at the last deploy. Use -f to deploy again.
#
# The build runs with GOMEMLIMIT=2GiB (or M2_BUILD_MEMORY), so that it fits on a shared server.
#
# The build keeps the rendered math in $M2_DEPLOY/cache, so that the next build renders only the new formulas.
#
# The file $M2_DEPLOY/cloudflare.env must set CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID. Keep it at mode 600.
# Bind the R2 bucket math2-social (or M2_SOCIAL_BUCKET) to Pages as SOCIAL_PACKS. The Pages deployment also contains the packs as a fallback.
set -eu

dir=${M2_DEPLOY:-$HOME/math2-deploy}
project=${M2_PAGES_PROJECT:-math2}
social_bucket=${M2_SOCIAL_BUCKET:-math2-social}
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

# sync fetches main of a repository into a directory. With "full", it keeps the whole history: the site reads the dates of the changes to the nodes from it, for the page Latest.
sync() {
	depth="--depth 1"
	[ "${3:-}" = full ] && depth=""
	if [ -d "$dir/$1/.git" ]; then
		if [ "${3:-}" = full ] && [ "$(git -C "$dir/$1" rev-parse --is-shallow-repository)" = true ]; then
			git -C "$dir/$1" fetch -q --unshallow origin main
		fi
		git -C "$dir/$1" fetch -q $depth origin main
		git -C "$dir/$1" reset -q --hard FETCH_HEAD
	else
		git clone -q $depth "https://github.com/tamnd/$2.git" "$dir/$1"
	fi
	git -C "$dir/$1" rev-parse HEAD
}

content=$(sync content math2 full)
toolchain=$(sync toolchain math2-agent)
wikipedia=$(sync wikipedia wikipedia-math)
state="$content $toolchain $wikipedia"
if [ "$force" != "-f" ] && [ -f "$dir/deployed" ] && [ "$(cat "$dir/deployed")" = "$state" ]; then
	exit 0
fi

echo "$(date -u +%FT%TZ) deploy math2 $content, math2-agent $toolchain, wikipedia-math $wikipedia"
(cd "$dir/toolchain" && go build -trimpath -o "$dir/m2" ./cmd/m2)
# The arXiv records are in tamnd/math2-records at the commit of manifests/records-arxiv.yaml (corpus arxiv AQ11). The site reads the tree with them. The records of an earlier deploy go first, since unpack adds nothing to a tree that has them.
recpin=$(sed -n 's/^commit: *//p' "$dir/content/manifests/records-arxiv.yaml" 2>/dev/null || true)
if [ -n "$recpin" ]; then
	git -C "$dir/content" clean -fdq records
	git -C "$dir/content" checkout -q -- records
	[ -d "$dir/records-arxiv/.git" ] || git init -q "$dir/records-arxiv"
	git -C "$dir/records-arxiv" fetch -q --depth 1 https://github.com/tamnd/math2-records "$recpin"
	git -C "$dir/records-arxiv" checkout -q -f FETCH_HEAD
	"$dir/m2" corpus records unpack -root "$dir/content" -out "$dir/records-arxiv"
fi
rm -rf "$dir/site"
GOMEMLIMIT=${M2_BUILD_MEMORY:-2GiB} "$dir/m2" site build -content "$dir/content" -spec "$dir/toolchain/spec" -wikipedia "$dir/wikipedia" -out "$dir/site" -url "$url" -commit "$content" -date now -cloudflare -cache "$dir/cache/math.gob.gz" -social-packs "$dir/social-packs"
files=$(find "$dir/site" -type f | wc -l)
big=$(find "$dir/site" -type f -size +24M | head -1)
if [ "$files" -gt "$limit" ] || [ -n "$big" ]; then
	echo "the site has $files files (the limit is $limit) or a file over 24 MB ($big). The deploy stops and the last deployment stays."
	exit 1
fi
python3 "$dir/toolchain/scripts/upload_social_packs.py" "$dir/social-packs" --bucket "$social_bucket"
npx --yes wrangler@4 pages deploy "$dir/site" --project-name "$project" --branch main --commit-hash "$content" --commit-message "math2 $content" --commit-dirty=true
echo "$state" >"$dir/deployed"
