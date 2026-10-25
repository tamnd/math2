"""Check the curricula in topics/curricula/ without the m2 toolchain.

Each file must agree with schema/curriculum.v1.json. The check also finds the errors that the schema cannot find: a curriculum whose name is not the name of its file, two courses with the same name, two items with the same name, a source that the file does not define, and a node tag that has no node file.

With --decls FILE, the check also reports each decl that is not a line of FILE. Make the file from the .ilean files of the Lean build. CI does not use this option, because CI does not build Mathlib.

Usage: python check_curricula.py [--decls FILE] [root]
"""

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from check_nodes import TAG, Loader

SCHEMA = Path(__file__).resolve().parents[2] / "schema" / "curriculum.v1.json"


def curriculum_errors(path, data, validator, root, decls=None):
    """Return the errors of one curriculum, one line each."""
    errors = []
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        where = ".".join(str(p) for p in err.absolute_path) or "file"
        errors.append(f"{path}: {where}: {err.message}")
    if errors or not isinstance(data, dict):
        return errors
    if data["curriculum"] != path.stem:
        errors.append(f"{path}: the curriculum is {data['curriculum']!r}, and the name of the file is {path.stem!r}")
    sources = data["sources"]
    courses, names = set(), {}
    for course in data["courses"]:
        cid = course["course"]
        if cid in courses:
            errors.append(f"{path}: the course {cid!r} occurs two times")
        courses.add(cid)
        for number, item in enumerate(course["items"], 1):
            where = f"{path}: {cid} item {number} ({item['name']})"
            key = item["name"].casefold()
            if key in names:
                errors.append(f"{where}: the name is also the name of {names[key]}")
            names[key] = f"{cid} item {number}"
            if "wikipedia" in item and "wikipedia" not in sources:
                errors.append(f"{where}: the file defines no source wikipedia")
            if "wikidata" in item and "wikipedia" not in item:
                errors.append(f"{where}: the item has a wikidata item and no wikipedia title")
            for name in item.get("mathlib", []):
                if name not in sources:
                    errors.append(f"{where}: the file defines no source {name!r}")
            tag = item.get("node")
            if tag and TAG.match(tag) and not (root / "nodes" / tag[:2] / f"{tag}.md").is_file():
                errors.append(f"{where}: the node {tag} does not exist")
            if decls is not None and "decl" in item and item["decl"] not in decls:
                errors.append(f"{where}: the decl {item['decl']} is not in the declaration list")
    return errors


def main(argv):
    decls = None
    if len(argv) >= 2 and argv[0] == "--decls":
        decls = set(Path(argv[1]).read_text(encoding="utf-8").split())
        argv = argv[2:]
    root = Path(argv[0]) if argv else Path(".")
    validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    errors, count = [], 0
    for path in sorted((root / "topics" / "curricula").glob("*.yaml")):
        rel = path.relative_to(root)
        try:
            data = yaml.load(path.read_text(encoding="utf-8"), Loader=Loader)
        except yaml.YAMLError as err:
            errors.append(f"{rel}: the file is not YAML: {err}")
            continue
        errors += curriculum_errors(rel, data, validator, root, decls)
        if isinstance(data, dict):
            count += sum(len(c.get("items", [])) for c in data.get("courses", []) if isinstance(c, dict))
    for line in errors:
        print(line)
    print(f"{count} items, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
