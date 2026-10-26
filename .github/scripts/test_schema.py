"""Check that schema/node.v1.json is consistent with itself."""

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

SCHEMA = Path(__file__).resolve().parents[2] / "schema" / "node.v1.json"


class SchemaTest(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    def test_valid_json_schema(self):
        Draft202012Validator.check_schema(self.schema)

    def test_order_has_each_key_one_time(self):
        keys = set(self.schema["properties"])
        for branch in self.schema["allOf"]:
            keys |= set(branch["then"]["properties"])
        order = self.schema["x-m2-order"]
        self.assertEqual(len(order), len(set(order)), "a key occurs two times in x-m2-order")
        self.assertEqual(sorted(keys), sorted(order))

    def test_sections_for_each_kind(self):
        kinds = self.schema["properties"]["kind"]["enum"]
        branches = {b["if"]["properties"]["kind"]["const"]: b["then"] for b in self.schema["allOf"]}
        self.assertEqual(sorted(kinds), sorted(branches))
        for kind, then in branches.items():
            with self.subTest(kind=kind):
                sections = then["x-m2-sections"]
                self.assertTrue(set(sections["required"]) <= set(sections["allowed"]))

    def test_23_edge_types(self):
        self.assertEqual(len({e["name"] for e in self.schema["x-m2-edges"]}), 23)


class OtherSchemasTest(unittest.TestCase):
    def test_valid_json_schemas(self):
        for name in ["computation.v1.json", "curriculum.v1.json", "review.v1.json", "skeleton.v1.json"]:
            with self.subTest(name):
                Draft202012Validator.check_schema(json.loads((SCHEMA.parent / name).read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
