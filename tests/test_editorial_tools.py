import unittest
from youtube_agent.editorial_tools import generate_hook_variants, draft_chapters, classify_comment

class EditorialToolsTests(unittest.TestCase):
    def test_hook_count_and_topic(self):
        hooks=generate_hook_variants("solar panels")
        self.assertEqual(len(hooks),5)
        self.assertTrue(all("solar panels" in h["hook"] for h in hooks))

    def test_chapters_use_supplied_timestamps_only(self):
        result=draft_chapters([{"start":65,"text":"Intro to the subject"},{"text":"no timestamp"}])
        self.assertEqual(result[0]["timestamp"],"01:05")
        self.assertEqual(len(result),1)

    def test_comment_labels(self):
        self.assertEqual(classify_comment("Great video, thank you"),"positive")
        self.assertEqual(classify_comment("Where can I learn?"),"question")
        self.assertEqual(classify_comment("This is fake"),"possible_criticism")

if __name__ == "__main__":
    unittest.main()
