#!/usr/bin/env python3
"""Write the field node of each item of the seed list and the skeletons whose node exists.

An item matches a node when the key of the item name is the key of the node name or of an alias of the node, and exactly one node of a kind that fits the kind of the item has the key.
The key ignores case, accents, punctuation, the article "the", the possessive 's, a final plural s and the spellings colour/color and -ise/-ize.
The script does not match by the Wikipedia title or the Wikidata item: many items share the article of a broader concept, for example "orthogonal Lie algebra" and "orthogonal group".
The script changes only the lines of the items without a node. It keeps the other lines as they are.

Usage: python scripts/link_items.py [--dry-run] [FILE ...]
"""
import argparse
import collections
import glob
import re
import sys
import unicodedata

import yaml

FITS = {
    "concept": ("concept", "definition"),
    "definition": ("concept", "definition"),
    "statement": ("statement",),
    "conjecture": ("conjecture", "problem", "statement"),
    "problem": ("problem", "conjecture"),
    "example": ("example", "object", "concept"),
    "counterexample": ("counterexample", "example"),
    "object": ("object", "concept", "example"),
    "proof": ("proof",),
    "computation": ("computation",),
    "topic": ("topic", "concept"),
}
ITEM = re.compile(r"^(\s*- \{)(.*)(\}\s*)$")


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = s.replace("'s ", "s ").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def key(s):
    words = []
    for w in slug(s).split("-"):
        if w in ("the", "a", "an"):
            continue
        w = w.replace("colour", "color").replace("isation", "ization")
        w = re.sub(r"is(e|ed|es|ing)$", r"iz\1", w) if len(w) > 5 else w
        if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
            w = w[:-1]
        words.append(w)
    return "-".join(words)


def read_nodes():
    nodes = []
    for f in glob.glob("nodes/*/*.md"):
        text = open(f, encoding="utf-8").read()
        if not text.startswith("---"):
            continue
        fm = yaml.safe_load(text.split("---", 2)[1]) or {}
        if fm.get("status") == "retired" or fm.get("retired"):
            continue
        nodes.append({
            "tag": str(fm["tag"]),
            "kind": fm.get("kind"),
            "slugs": {key(str(fm.get("name", "")))} | {key(str(a)) for a in fm.get("aliases") or []},
        })
    return nodes


def index(nodes):
    ix = collections.defaultdict(list)
    for n in nodes:
        for v in n["slugs"]:
            if v:
                ix[v].append(n)
    return ix


def pick(cands, kind):
    fits = FITS.get(kind, (kind,))
    cands = [c for c in cands if c["kind"] in fits]
    if not cands:
        return None
    # Prefer the first kind of the list, for example a concept for a definition item.
    for k in fits:
        best = [c for c in cands if c["kind"] == k]
        if best:
            return best[0]["tag"] if len(best) == 1 else None
    return None


def link_file(path, by_key, dry):
    lines = open(path, encoding="utf-8").read().split("\n")
    stats = collections.Counter()
    for i, line in enumerate(lines):
        m = ITEM.match(line)
        if not m:
            continue
        item = yaml.safe_load("{" + m.group(2) + "}")
        if not isinstance(item, dict) or "name" not in item:
            continue
        stats["items"] += 1
        if item.get("node"):
            stats["had"] += 1
            continue
        tag = pick(by_key.get(key(item["name"]), []), item.get("kind"))
        if not tag:
            continue
        stats["new"] += 1
        lines[i] = m.group(1) + m.group(2) + ", node: " + tag + m.group(3)
    if not dry:
        open(path, "w", encoding="utf-8").write("\n".join(lines))
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    files = a.files or ["topics/curricula/seed.yaml"] + sorted(glob.glob("topics/skeletons/*.yaml"))
    nodes = read_nodes()
    by_key = index(nodes)
    total = collections.Counter()
    for f in files:
        s = link_file(f, by_key, a.dry_run)
        total += s
        print(f"{f}: {s['had'] + s['new']}/{s['items']} items have a node ({s['new']} new)")
    linked = total["had"] + total["new"]
    print(f"total: {linked}/{total['items']} items have a node")


if __name__ == "__main__":
    sys.exit(main())
