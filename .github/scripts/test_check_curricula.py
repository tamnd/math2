"""Tests for check_curricula.py. Run them with: python -m unittest discover -s .github/scripts"""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from check_curricula import main

GOOD = """curriculum: core
title: A core
sources:
  wikipedia: {title: English Wikipedia, url: "https://en.wikipedia.org/wiki/"}
  undergrad: {title: Mathlib undergrad.yaml, url: "https://github.com/leanprover-community/mathlib4"}
courses:
  - course: groups
    title: Group theory
    year: 2
    items:
      - {name: group, kind: definition, decl: Group, wikipedia: Group (mathematics), wikidata: Q83478, mathlib: [undergrad]}
      - {name: Lagrange's theorem, kind: statement, wikipedia: "Lagrange's theorem (group theory)"}
"""


class CheckCurriculaTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)

    def tearDown(self):
        self.dir.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def run_check(self, *args):
        out = io.StringIO()
        with redirect_stdout(out):
            code = main([*args, str(self.root)])
        return code, out.getvalue()

    def test_good(self):
        self.write("topics/curricula/core.yaml", GOOD)
        code, out = self.run_check()
        self.assertEqual(code, 0, out)
        self.assertIn("2 items, 0 errors", out)

    def test_errors(self):
        cases = {
            "an item without a source": (GOOD.replace(', wikipedia: "Lagrange\'s theorem (group theory)"', ""), "is not valid under any of the given schemas"),
            "a bad kind": (GOOD.replace("kind: statement", "kind: theorem"), "'theorem' is not one of"),
            "a name two times": (GOOD.replace("Lagrange's theorem", "Group"), "the name is also the name of groups item 1"),
            "a source that is not defined": (GOOD.replace("[undergrad]", "[overview]"), "the file defines no source 'overview'"),
            "the wrong file name": (GOOD.replace("curriculum: core", "curriculum: seed"), "the name of the file is 'core'"),
            "a node that does not exist": (GOOD.replace("mathlib: [undergrad]}", "mathlib: [undergrad], node: 7K3QX2}"), "the node 7K3QX2 does not exist"),
        }
        for name, (text, want) in cases.items():
            with self.subTest(name):
                self.write("topics/curricula/core.yaml", text)
                code, out = self.run_check()
                self.assertEqual(code, 1, out)
                self.assertIn(want, out)

    def test_decls(self):
        self.write("topics/curricula/core.yaml", GOOD)
        self.write("decls.txt", "Monoid\n")
        code, out = self.run_check("--decls", str(self.root / "decls.txt"))
        self.assertEqual(code, 1, out)
        self.assertIn("the decl Group is not in the declaration list", out)


if __name__ == "__main__":
    unittest.main()
