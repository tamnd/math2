"""Tests for check_nodes.py. Run them with: python -m unittest discover -s .github/scripts"""

import tempfile
import unittest
from pathlib import Path

from check_nodes import check

GOOD = """---
tag: {tag}
kind: statement
role: theorem
name: A statement
---

## Statement

See [[a group|{link}]].
"""


class CheckNodesTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)

    def tearDown(self):
        self.dir.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_no_nodes_directory(self):
        self.assertEqual(check(self.root), ([], 0))

    def test_good_nodes(self):
        self.write("nodes/7K/7K3QX2.md", GOOD.format(tag="7K3QX2", link="1H8D2C"))
        self.write("nodes/1H/1H8D2C.md", GOOD.format(tag="1H8D2C", link="7K3QX2"))
        self.assertEqual(check(self.root), ([], 2))

    def test_provisional_id(self):
        self.write("nodes/~/~3fa94c01.md", GOOD.format(tag="~3fa94c01", link="~3fa94c01"))
        self.assertEqual(check(self.root), ([], 1))

    def test_bad_tag_letter(self):
        self.write("nodes/7I/7I3QX2.md", GOOD.format(tag="7I3QX2", link="7I3QX2"))
        errors, _ = check(self.root)
        self.assertIn("is not a tag", errors[0])

    def test_wrong_shard(self):
        self.write("nodes/AB/7K3QX2.md", GOOD.format(tag="7K3QX2", link="7K3QX2"))
        errors, _ = check(self.root)
        self.assertIn("must be in nodes/7K/", errors[0])

    def test_tag_does_not_match_file_name(self):
        self.write("nodes/7K/7K3QX2.md", GOOD.format(tag="7K3QX3", link="7K3QX2"))
        errors, _ = check(self.root)
        self.assertIn("the file name says", errors[0])

    def test_unknown_kind(self):
        self.write("nodes/7K/7K3QX2.md", "---\ntag: 7K3QX2\nkind: lemma\nname: A lemma\n---\n")
        errors, _ = check(self.root)
        self.assertIn("is not one of the 11 kinds", errors[0])

    def test_no_front_matter(self):
        self.write("nodes/7K/7K3QX2.md", "## Statement\n")
        errors, _ = check(self.root)
        self.assertIn("must start with YAML front matter", errors[0])

    def test_dangling_link(self):
        self.write("nodes/7K/7K3QX2.md", GOOD.format(tag="7K3QX2", link="1H8D2C"))
        errors, _ = check(self.root)
        self.assertIn("does not exist", errors[0])


    def errors_for(self, front, body=""):
        self.write("nodes/7K/7K3QX2.md", f"---\ntag: 7K3QX2\n{front}---\n{body}")
        errors, _ = check(self.root)
        return errors

    def test_each_kind_is_valid(self):
        for kind, (front, body) in VALID.items():
            with self.subTest(kind=kind):
                self.assertEqual(self.errors_for(front, body), [])

    def test_each_kind_needs_its_fields(self):
        for kind, (front, body) in VALID.items():
            with self.subTest(kind=kind):
                missing = front.replace(f"kind: {kind}\n", f"kind: {kind}\nstatus: E5\n").replace("name: A node\n", "")
                errors = self.errors_for(missing, body)
                self.assertTrue(any("rule S03" in e for e in errors), errors)
                self.assertTrue(any("'name' is a required property" in e for e in errors), errors)

    def test_statement_needs_role(self):
        self.assertIn("'role' is a required property", " ".join(self.errors_for("kind: statement\nname: A node\n", "## Statement\n")))

    def test_field_of_another_kind(self):
        errors = self.errors_for("kind: statement\nrole: lemma\nname: A node\nproves: 1H8D2C\n", "## Statement\n")
        self.assertIn("'proves' was unexpected", " ".join(errors))

    def test_bad_msc_code(self):
        errors = self.errors_for("kind: statement\nrole: lemma\nname: A node\nmsc: [20E05]\n", "## Statement\n")
        self.assertIn("msc.0", " ".join(errors))

    def test_source_needs_one_identifier(self):
        front = 'kind: statement\nrole: lemma\nname: A node\nsources:\n  - doi: "10.1/x"\n    arxiv: "2106.09685v2"\n    locator: "p. 3"\n'
        self.assertIn("sources.0", " ".join(self.errors_for(front, "## Statement\n")))

    def test_unknown_section(self):
        errors = self.errors_for("kind: statement\nrole: lemma\nname: A node\n", "## Statement\n\n## Proof\n")
        self.assertIn("'Proof' is not one of", " ".join(errors))

    def test_missing_section(self):
        errors = self.errors_for("kind: definition\nname: A node\ndefines: 1H8D2C\n", "## Remarks\n")
        self.assertIn("'Definition' is missing", " ".join(errors))

    def test_section_order(self):
        errors = self.errors_for("kind: statement\nrole: lemma\nname: A node\n", "## Remarks\n\n## Statement\n")
        self.assertIn("must be in this order", " ".join(errors))

    def test_date_stays_a_string(self):
        front = "kind: statement\nrole: lemma\nname: A node\nretired:\n  date: 2026-10-25\n  reason: duplicate\n  successor: [1H8D2C]\n"
        self.assertEqual(self.errors_for(front, "## Statement\n"), [])


IMAGE = "m2-sage@sha256:" + "0" * 64

# A valid front matter and body for each of the 11 kinds. The tag line is added by the test.
VALID = {
    "concept": ("kind: concept\nname: A node\n", "## Summary\n"),
    "definition": ("kind: definition\nname: A node\ndefines: 1H8D2C\n", "## Definition\n"),
    "statement": ("kind: statement\nname: A node\nrole: theorem\n", "## Statement\n\n## Remarks\n"),
    "conjecture": ("kind: conjecture\nname: A node\n", "## Statement\n"),
    "problem": ("kind: problem\nname: A node\n", "## Problem\n"),
    "example": ("kind: example\nname: A node\ninstance_of: [1H8D2C]\n", "## Example\n"),
    "counterexample": ("kind: counterexample\nname: A node\n", "## Counterexample\n"),
    "object": ("kind: object\nname: A node\n", "## Description\n"),
    "proof": ("kind: proof\nname: A node\nproves: 1H8D2C\n", "## Proof\n\n## Idea\n"),
    "computation": (f"kind: computation\nname: A node\nclaim: x\nengine:\n  image: {IMAGE}\n  entry: run.py\n", "## Description\n"),
    "topic": ("kind: topic\nname: A node\n", ""),
}

if __name__ == "__main__":
    unittest.main()
