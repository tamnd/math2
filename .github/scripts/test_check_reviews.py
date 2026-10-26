"""Tests for check_reviews.py. Run them with: python -m unittest discover -s .github/scripts"""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from check_reviews import main

H1 = "blake3:" + "1" * 64
H2 = "blake3:" + "2" * 64

GOOD = f"""reviews:
  - id: r-3C53TD-01
    reviewer: github:octocat
    date: 2026-12-01
    decl: Math2.Match.lagrange
    statement_hash: "{H1}"
    type_hash: "{H2}"
    verdict: faithful-with-conventions
    conventions: [the order of a finite group is Nat.card]
  - id: r-3C53TD-02
    reviewer: orcid:0000-0002-1825-0097
    date: 2026-12-02
    decl: Math2.Match.lagrange
    statement_hash: "{H1}"
    type_hash: "{H2}"
    verdict: not-faithful
    class: M-hyp-missing
    notes: The subgroup is not finite.
"""

REVIEWERS = """# reviewer first areas affiliations
github:octocat 2026-12-01 20D ror:03vek6s52
orcid:0000-0002-1825-0097 2026-12-02 20D -
"""


class CheckReviewsTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)
        self.write("nodes/3C5/3C53TD.md", "---\ntag: 3C53TD\n---\n")
        self.write("registers/reviewers.reg", REVIEWERS)

    def tearDown(self):
        self.dir.cleanup()

    def write(self, rel, text):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def run_check(self):
        out = io.StringIO()
        with redirect_stdout(out):
            code = main([str(self.root)])
        return code, out.getvalue()

    def test_good(self):
        self.write("reviews/3C5/3C53TD.yaml", GOOD)
        code, out = self.run_check()
        self.assertEqual(code, 0, out)
        self.assertIn("2 reviews, 0 errors", out)

    def test_no_reviews(self):
        code, out = self.run_check()
        self.assertEqual(code, 0, out)
        self.assertIn("0 reviews, 0 errors", out)

    def test_errors(self):
        cases = {
            "unknown reviewer": (GOOD.replace("github:octocat", "github:someone"), "has no record"),
            "wrong id": (GOOD.replace("r-3C53TD-02", "r-G5S1M9-02"), "must start with r-3C53TD-"),
            "same id": (GOOD.replace("r-3C53TD-02", "r-3C53TD-01"), "is also in"),
            "no class": (GOOD.replace("    class: M-hyp-missing\n", ""), "'class' is a required property"),
            "class on a positive verdict": (GOOD.replace("conventions: [the order of a finite group is Nat.card]", "conventions: [x]\n    class: M-def"), "should not be valid"),
            "no conventions": (GOOD.replace("    conventions: [the order of a finite group is Nat.card]\n", ""), "'conventions' is a required property"),
            "bad hash": (GOOD.replace(H2, "blake3:abc", 1), "does not match"),
            "bad verdict": (GOOD.replace("verdict: not-faithful", "verdict: wrong"), "is not one of"),
            "unknown field": (GOOD.replace("    notes:", "    score: 3\n    notes:"), "Additional properties"),
        }
        for name, (text, want) in cases.items():
            with self.subTest(name):
                self.write("reviews/3C5/3C53TD.yaml", text)
                code, out = self.run_check()
                self.assertEqual(code, 1, out)
                self.assertIn(want, out)

    def test_path(self):
        cases = {
            "wrong shard": "reviews/G5S/3C53TD.yaml",
            "no shard": "reviews/3C53TD.yaml",
            "no node": "reviews/G5S/G5S1M8.yaml",
        }
        for name, rel in cases.items():
            with self.subTest(name):
                self.write(rel, GOOD)
                code, out = self.run_check()
                self.assertEqual(code, 1, out)
                (self.root / rel).unlink()


if __name__ == "__main__":
    unittest.main()
