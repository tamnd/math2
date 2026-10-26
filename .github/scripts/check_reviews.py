"""Check the fidelity reviews in reviews/ without the m2 toolchain.

Each file must agree with schema/review.v1.json. The check also finds the errors that the schema cannot find: a file that is not at reviews/<shard>/<tag>.yaml, a review id that does not start with the tag of its file, an id that occurs two times, a review of a node that does not exist, and a reviewer that has no record in registers/reviewers.reg.

The hashes are not checked here. m2 audit checks them against the build (rules V01 and F02).

Usage: python check_reviews.py [root]
"""

import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from check_nodes import SHARD_LEN, TAG, Loader, read_register

SCHEMA = Path(__file__).resolve().parents[2] / "schema" / "review.v1.json"


def review_errors(rel, data, validator, root, reviewers, seen):
    """Return the errors of one review file, one line each. seen maps each review id to the file that has it."""
    errors = []
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        where = ".".join(str(p) for p in err.absolute_path) or "file"
        errors.append(f"{rel}: {where}: {err.message}")
    tag = rel.stem
    if len(rel.parts) != 3 or not TAG.match(tag) or rel.parts[1] != tag[:SHARD_LEN]:
        errors.append(f"{rel}: the file must be reviews/<shard>/<tag>.yaml, and the shard is the first three characters of the tag")
    elif not (root / "nodes" / tag[:SHARD_LEN] / f"{tag}.md").is_file():
        errors.append(f"{rel}: the node {tag} does not exist")
    if errors or not isinstance(data, dict):
        return errors
    for number, review in enumerate(data["reviews"], 1):
        where = f"{rel}: review {number} ({review['id']})"
        if not review["id"].startswith(f"r-{tag}-"):
            errors.append(f"{where}: the id must start with r-{tag}-")
        if review["id"] in seen:
            errors.append(f"{where}: the id is also in {seen[review['id']]}")
        seen[review["id"]] = rel
        if review["reviewer"] not in reviewers:
            errors.append(f"{where}: the reviewer {review['reviewer']} has no record in registers/reviewers.reg")
    return errors


def main(argv):
    root = Path(argv[0]) if argv else Path(".")
    validator = Draft202012Validator(json.loads(SCHEMA.read_text(encoding="utf-8")))
    reviewers = {fields[0] for _, fields in read_register(root / "registers" / "reviewers.reg")}
    errors, count, seen = [], 0, {}
    for path in sorted((root / "reviews").rglob("*.yaml")):
        rel = path.relative_to(root)
        try:
            data = yaml.load(path.read_text(encoding="utf-8"), Loader=Loader)
        except yaml.YAMLError as err:
            errors.append(f"{rel}: the file is not YAML: {err}")
            continue
        errors += review_errors(rel, data, validator, root, reviewers, seen)
        if isinstance(data, dict) and isinstance(data.get("reviews"), list):
            count += len(data["reviews"])
    for line in errors:
        print(line)
    print(f"{count} reviews, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
