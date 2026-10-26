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

SKELETON = """skeleton: 20-XX
title: Group theory
sources:
  wikipedia: {title: English Wikipedia, url: "https://en.wikipedia.org/wiki/"}
items:
  - {name: group, kind: concept, wikipedia: Group (mathematics), wikidata: Q83478}
  - {name: Sylow theorems, kind: statement, wikipedia: Sylow theorems}
  - {name: simple group, kind: definition, wikipedia: Simple group}
"""

MSC = '"11-XX": {label: number theory}\n"20-XX": {label: groups}\n'


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


    def test_skeleton(self):
        self.write("topics/msc2020.yaml", MSC)
        self.write("topics/curricula/core.yaml", GOOD)
        self.write("topics/skeletons/20.yaml", SKELETON)
        code, out = self.run_check()
        self.assertEqual(code, 0, out)
        self.assertIn("5 items, 0 errors", out)

    def test_skeleton_errors(self):
        self.write("topics/msc2020.yaml", MSC)
        cases = {
            "the wrong file name": ("11.yaml", SKELETON, "the skeleton is '20-XX', and the name of the file is '11'"),
            "a code that is not top-level": ("20.yaml", SKELETON.replace("20-XX", "20Axx"), "does not match"),
            "a code that is not in the map": ("30.yaml", SKELETON.replace("20-XX", "30-XX"), "the code 30-XX is not in topics/msc2020.yaml"),
            "a name two times": ("20.yaml", SKELETON.replace("simple group", "Group"), "the name is also the name of item 1"),
            "an item without a source": ("20.yaml", SKELETON.replace(", wikipedia: Simple group", ""), "is not valid under any of the given schemas"),
            "a source that is not defined": ("20.yaml", SKELETON.replace("Sylow theorems}", "Sylow theorems, mathlib: [undergrad]}"), "the file defines no source 'undergrad'"),
            "a node that does not exist": ("20.yaml", SKELETON.replace("Simple group}", "Simple group, node: 7K3QX2}"), "the node 7K3QX2 does not exist"),
            "an unknown field": ("20.yaml", SKELETON.replace("title: Group theory", "title: Group theory\nreview: yes"), "Additional properties are not allowed"),
        }
        for name, (file, text, want) in cases.items():
            with self.subTest(name):
                path = self.root / "topics" / "skeletons" / file
                self.write(path.relative_to(self.root), text)
                code, out = self.run_check()
                path.unlink()
                self.assertEqual(code, 1, out)
                self.assertIn(want, out)


if __name__ == "__main__":
    unittest.main()
