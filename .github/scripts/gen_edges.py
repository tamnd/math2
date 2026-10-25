"""Generate schema/edges.md from the x-m2-edges list in schema/node.v1.json.

Run it with no arguments to write the file. Run it with --check to fail when the file is out of date.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schema" / "node.v1.json"
OUT = ROOT / "schema" / "edges.md"

GROUPS = {
    "logical": "Logical edges carry truth. The build uses them for the AND-OR dependency closure.",
    "conceptual": "Conceptual edges carry meaning. They are for navigation and search, and they do not change status.",
    "record": "Record edges carry provenance and identity.",
}


def render(schema):
    lines = [
        "# Edge types",
        "",
        "This file is generated from `node.v1.json` by `.github/scripts/gen_edges.py`. Do not edit it.",
        "",
        "A node file stores each edge that touches it in a front matter field. The table gives the field. The `cites` edge has no field, because it exists only between records.",
    ]
    for group, text in GROUPS.items():
        lines += ["", f"## {group.capitalize()}", "", text, "", "| Edge | From | To | Field |", "|---|---|---|---|"]
        for e in schema["x-m2-edges"]:
            if e["group"] == group:
                field = f"`{e['field']}`" if e["field"] else "none"
                lines.append(f"| `{e['name']}` | {e['from']} | {e['to']} | {field} |")
    return "\n".join(lines) + "\n"


def main():
    text = render(json.loads(SCHEMA.read_text(encoding="utf-8")))
    if "--check" in sys.argv[1:]:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("schema/edges.md is out of date. Run python .github/scripts/gen_edges.py.")
            return 1
        return 0
    OUT.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
