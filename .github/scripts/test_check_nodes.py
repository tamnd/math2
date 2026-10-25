"""Tests for check_nodes.py. Run them with: python -m unittest discover -s .github/scripts"""

import tempfile
import unittest
from pathlib import Path

from check_nodes import check

GOOD = """---
tag: {tag}
kind: statement
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
        self.write("nodes/7K/7K3QX2.md", "---\ntag: 7K3QX2\nkind: lemma\n---\n")
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


if __name__ == "__main__":
    unittest.main()
