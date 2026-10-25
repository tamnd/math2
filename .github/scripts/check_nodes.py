"""Check the node files in nodes/ without the m2 toolchain.

This check needs only Python, PyYAML and jsonschema. It finds the errors that a person can make with a text editor: a bad tag, a file in the wrong shard, front matter that does not agree with schema/node.v1.json, a body section that the kind does not have, or a link to a node that does not exist. The full audit is `m2 audit` in tamnd/math2-agent.

Usage: python check_nodes.py [root]
"""

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

SCHEMA = Path(__file__).resolve().parents[2] / "schema" / "node.v1.json"

# Crockford base32 without I, L, O and U.
TAG = re.compile(r"^[0-9A-HJKMNP-TV-Z]{6}$")
PROVISIONAL = re.compile(r"^~[0-9a-f]{8}$")
LINK = re.compile(r"\[\[([^\]|]+)\|([^\]]+)\]\]")
SECTION = re.compile(r"^## (.+?)\s*$", re.MULTILINE)

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


class Loader(yaml.SafeLoader):
    """A safe loader that reads values as m2 reads them.

    Dates stay strings. A number such as 20E05 is a float, as in YAML 1.2, so that an MSC code without quotes fails here and in m2.
    """


Loader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
Loader.add_implicit_resolver("tag:yaml.org,2002:float", re.compile(r"^[-+]?[0-9]+[eE][-+]?[0-9]+$"), list("-+0123456789"))


def load_schema(path=SCHEMA):
    """Return the validator, the forbidden field names and the sections of each kind."""
    schema = json.loads(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    forbidden = set(schema["propertyNames"]["not"]["enum"])
    sections = {}
    for branch in schema["allOf"]:
        kind = branch["if"]["properties"]["kind"]["const"]
        sections[kind] = branch["then"]["x-m2-sections"]
    return validator, forbidden, sections


def schema_errors(meta, validator, forbidden):
    """Return the schema errors for one front matter mapping, one line each."""
    errors = [f"the field {key!r} is not allowed, because the build computes status (rule S03)" for key in meta if key in forbidden]
    for err in sorted(validator.iter_errors(meta), key=lambda e: list(e.absolute_path)):
        # The caller reports a bad kind with a shorter message.
        if err.validator == "propertyNames" or list(err.absolute_path) == ["kind"]:
            continue
        where = ".".join(str(p) for p in err.absolute_path) or "front matter"
        errors.append(f"{where}: {err.message}")
    return errors


def section_errors(body, rule):
    """Return the errors for the level 2 headings of a body. The schema gives the rule for each kind."""
    found = SECTION.findall(body)
    allowed = rule["allowed"]
    errors = [f"the section {name!r} is not one of {allowed}" for name in found if name not in allowed]
    errors += [f"the section {name!r} is missing" for name in rule["required"] if name not in found]
    known = [name for name in found if name in allowed]
    if known != sorted(known, key=allowed.index):
        errors.append(f"the sections must be in this order: {allowed}")
    if len(set(found)) != len(found):
        errors.append("a section occurs more than one time")
    return errors


def split_front_matter(text):
    """Return the front matter and the body, or None when the file has no front matter."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return text[4:end], text[end + 5 :]


def check(root, schema=SCHEMA):
    """Return a list of errors and the number of node files under root."""
    validator, forbidden, sections = load_schema(schema)
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
            meta = yaml.load(head, Loader=Loader)
        except yaml.YAMLError as err:
            errors.append(f"{rel}: the front matter is not valid YAML: {err}")
            continue
        if not isinstance(meta, dict):
            errors.append(f"{rel}: the front matter must be a mapping")
            continue
        if str(meta.get("tag")) != node_id:
            errors.append(f"{rel}: tag is {meta.get('tag')!r}, but the file name says {node_id!r}")
        kind = meta.get("kind")
        if kind not in KINDS:
            errors.append(f"{rel}: kind {kind!r} is not one of the 11 kinds")
        errors += [f"{rel}: {err}" for err in schema_errors(meta, validator, forbidden)]
        if kind in sections:
            errors += [f"{rel}: {err}" for err in section_errors(body, sections[kind])]
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
