import json
import os
import unittest
from unittest.mock import patch

from youtube_agent.ai_prompts import ideas_prompt, script_prompt
from youtube_agent.ai_provider import ProviderError, generate_json


class AIPromptTests(unittest.TestCase):
    def test_script_prompt_includes_context_and_duration(self):
        p = script_prompt("Topic", "Audience", "Angle", [{"url": "https://example.com"}], 7)
        self.assertIn("Topic", p)
        self.assertIn("duration_minutes", p)
        self.assertIn("7", p)

    def test_ideas_prompt_requests_distinct_ideas(self):
        p = ideas_prompt("Niche", "Audience", {"avoid": "duplicate"})
        self.assertIn("Generate 10", p)
        self.assertIn("Niche", p)


class AIProviderTests(unittest.TestCase):
    def test_missing_key_fails_without_network(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ProviderError):
                generate_json("prompt")

    def test_rejects_non_object_json(self):
        class FakeResponse:
            def __enter__(self):
                return self
            def __exit__(self, *args):
                return False
            def read(self):
                response = {"choices": [{"message": {"content": "[1, 2]"}}]}
                return json.dumps(response).encode()

        with patch.dict(os.environ, {"OPENAI_API_KEY": "test"}, clear=True), patch(
            "youtube_agent.ai_provider.urlopen", return_value=FakeResponse()
        ):
            with self.assertRaises(ProviderError):
                generate_json("prompt")

    def test_parses_json_response(self):
        class FakeResponse:
            def __enter__(self):
                return self

            def __exit__(self, *args):
                return False

            def read(self):
                message = json.dumps({"ok": True})
                response = {"choices": [{"message": {"content": message}}]}
                return json.dumps(response).encode()

        with patch.dict(os.environ, {"OPENAI_API_KEY": "test"}, clear=True), patch(
            "youtube_agent.ai_provider.urlopen", return_value=FakeResponse()
        ):
            self.assertEqual(generate_json("prompt"), {"ok": True})


if __name__ == "__main__":
    unittest.main()
