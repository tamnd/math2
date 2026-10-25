"""Check the node files in nodes/ without the m2 toolchain.

This check needs only Python and PyYAML. It finds the errors that a person can make with a text editor: a bad tag, a file in the wrong shard, bad front matter, an unknown kind or a link to a node that does not exist. The full audit is `m2 audit` in tamnd/math2-agent.

Usage: python check_nodes.py [root]
"""

import re
import sys
from pathlib import Path

import yaml

# Crockford base32 without I, L, O and U.
TAG = re.compile(r"^[0-9A-HJKMNP-TV-Z]{6}$")
PROVISIONAL = re.compile(r"^~[0-9a-f]{8}$")
LINK = re.compile(r"\[\[([^\]|]+)\|([^\]]+)\]\]")

KINDS = {
    "concept",
    "definition",
    "statement",
    "conjecture",
    "problem",
    "example",
    "counterexample",
    "object",
    "proof",
    "computation",
    "topic",
}


def split_front_matter(text):
    """Return the front matter and the body, or None when the file has no front matter."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return text[4:end], text[end + 5 :]


def check(root):
    """Return a list of errors for the node files under root."""
    errors = []
    nodes_dir = root / "nodes"
    if not nodes_dir.is_dir():
        return errors, 0

    files = sorted(p for p in nodes_dir.rglob("*") if p.is_file())
    ids = set()
    parsed = []
    for path in files:
        rel = path.relative_to(root)
        if path.suffix != ".md":
            errors.append(f"{rel}: only .md files can be in nodes/")
            continue
        node_id = path.stem
        is_tag = bool(TAG.match(node_id))
        if not is_tag and not PROVISIONAL.match(node_id):
            errors.append(f"{rel}: {node_id!r} is not a tag or a provisional id")
            continue
        shard = path.parent.name
        want = node_id[:2] if is_tag else "~"
        if path.parent.parent != nodes_dir or shard != want:
            errors.append(f"{rel}: the file must be in nodes/{want}/")
        ids.add(node_id)
        parsed.append((path, rel, node_id))

    for path, rel, node_id in parsed:
        parts = split_front_matter(path.read_text(encoding="utf-8"))
        if parts is None:
            errors.append(f"{rel}: the file must start with YAML front matter between two --- lines")
            continue
        head, body = parts
        try:
            meta = yaml.safe_load(head)
        except yaml.YAMLError as err:
            errors.append(f"{rel}: the front matter is not valid YAML: {err}")
            continue
        if not isinstance(meta, dict):
            errors.append(f"{rel}: the front matter must be a mapping")
            continue
        if str(meta.get("tag")) != node_id:
            errors.append(f"{rel}: tag is {meta.get('tag')!r}, but the file name says {node_id!r}")
        if meta.get("kind") not in KINDS:
            errors.append(f"{rel}: kind {meta.get('kind')!r} is not one of the 11 kinds")
        for _, target in LINK.findall(body):
            if target not in ids:
                errors.append(f"{rel}: the link to {target!r} goes to a node that does not exist")

    return errors, len(parsed)


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path(".")
    errors, count = check(root)
    for error in errors:
        print(error)
    print(f"{count} node files checked, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
