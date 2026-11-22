import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SkillRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / "config" / "skills.json").read_text(encoding="utf-8"))

    def test_skill_ids_are_unique(self):
        ids = [skill["id"] for skill in self.registry["skills"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_registered_skill_has_instructions(self):
        for skill in self.registry["skills"]:
            path = ROOT / "skills" / skill["id"] / "SKILL.md"
            self.assertTrue(path.is_file(), f"Missing instructions: {path}")
            content = path.read_text(encoding="utf-8")
            self.assertRegex(content, rf"(?m)^name: {re.escape(skill['id'])}$")

    def test_status_values_are_valid(self):
        allowed = {"planned", "implemented_partial", "implemented", "blocked"}
        for skill in self.registry["skills"]:
            self.assertIn(skill["status"], allowed, skill["id"])


if __name__ == "__main__":
    unittest.main()
