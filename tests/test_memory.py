import json
import tempfile
import unittest
from pathlib import Path

from youtube_agent.memory import ChannelMemory


class MemoryTests(unittest.TestCase):
    def test_defaults_when_file_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            memory = ChannelMemory(Path(tmp) / "memory.json")
            self.assertEqual(memory.load()["idea_history"], [])

    def test_profile_save_load(self):
        with tempfile.TemporaryDirectory() as tmp:
            memory = ChannelMemory(Path(tmp) / "memory.json")
            memory.update_profile({"channel_name": "Test"})
            self.assertEqual(memory.load()["channel_profile"], {"channel_name": "Test"})

    def test_append_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            memory = ChannelMemory(Path(tmp) / "memory.json")
            memory.append_record("idea_history", {"title": "Idea"})
            self.assertEqual(memory.load()["idea_history"], [{"title": "Idea"}])

    def test_invalid_section(self):
        with tempfile.TemporaryDirectory() as tmp:
            memory = ChannelMemory(Path(tmp) / "memory.json")
            with self.assertRaises(ValueError):
                memory.append_record("channel_profile", {})

    def test_rejects_invalid_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            memory = ChannelMemory(Path(tmp) / "memory.json")
            with self.assertRaises(ValueError):
                memory.save([])
