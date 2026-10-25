"""Check that macros/m2.sty and macros/m2.katex.json define the same macros with the same expansion."""

import json
import re
import unittest
from pathlib import Path

MACROS = Path(__file__).resolve().parents[2] / "macros"
NEWCOMMAND = re.compile(r"^\\newcommand\{(\\[A-Za-z]+)\}(?:\[([1-9])\])?\{(.*)\}$")


def read_sty(path):
    """Return a map from each macro name to its argument count and expansion."""
    macros = {}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line.startswith("\\newcommand"):
            continue
        match = NEWCOMMAND.match(line)
        if match is None:
            raise ValueError(f"{path.name}:{number}: write each \\newcommand on one line in the form \\newcommand{{\\name}}[n]{{body}}")
        name, args, body = match.groups()
        if name in macros:
            raise ValueError(f"{path.name}:{number}: {name} is defined two times")
        macros[name] = (int(args or 0), body)
    return macros


def arg_count(body):
    """KaTeX gets the argument count from the highest #n in the expansion."""
    return max((int(n) for n in re.findall(r"#([1-9])", body)), default=0)


class MacrosTest(unittest.TestCase):
    def test_same_macros(self):
        sty = read_sty(MACROS / "m2.sty")
        katex = json.loads((MACROS / "m2.katex.json").read_text(encoding="utf-8"))
        self.assertTrue(sty, "m2.sty defines no macros")
        self.assertEqual(sorted(sty), sorted(katex), "the two files do not define the same macros")
        for name, (args, body) in sty.items():
            with self.subTest(macro=name):
                self.assertEqual(katex[name], body)
                self.assertEqual(arg_count(body), args)


if __name__ == "__main__":
    unittest.main()
