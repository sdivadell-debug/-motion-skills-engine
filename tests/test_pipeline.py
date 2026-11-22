import unittest
from youtube_agent.pipeline import execute_pipeline

class PipelineTests(unittest.TestCase):
    def test_stages_run_without_fabricating_unavailable_outputs(self):
        result = execute_pipeline({"topic": "Example", "profile": {}, "research_items": [], "competitor_videos": [], "ideas": []})
        self.assertEqual(result["stages"]["research"]["status"], "complete")
        self.assertEqual(result["stages"]["idea_lab"]["result"]["ranked_ideas"], [])
        self.assertEqual(result["stages"]["script_studio"]["status"], "not_executable")
        self.assertEqual(result["publishing"], "disabled")

    def test_research_invalid_claim_recorded_as_gap(self):
        result = execute_pipeline({"topic": "Example", "research_items": [{"claim": "x"}]})
        item = result["stages"]["research"]["result"]["items"][0]
        self.assertTrue(item["validation_errors"])

    def test_invalid_topic(self):
        with self.assertRaises(ValueError):
            execute_pipeline({"topic": ""})

if __name__ == "__main__":
    unittest.main()
