import unittest
from youtube_agent.pipeline import execute_pipeline

class PipelineTests(unittest.TestCase):
    def test_implemented_stages_and_guard(self):
        result = execute_pipeline({"topic": "Example", "profile": {}, "research_items": [], "competitor_videos": [], "ideas": [], "transcript_segments": [], "description_facts": [], "keywords": [], "performance_videos": [], "comments": [], "tasks": []})
        self.assertEqual(result["stages"]["research"]["status"], "complete")
        self.assertEqual(result["stages"]["idea_lab"]["result"]["ranked_ideas"], [])
        self.assertEqual(result["stages"]["script_studio"]["status"], "complete")
        self.assertEqual(result["stages"]["packaging"]["status"], "complete")
        self.assertEqual(result["stages"]["seo_publisher"]["status"], "complete")
        self.assertEqual(result["stages"]["creator_review"]["status"], "approval_required")
        self.assertEqual(result["publishing"], "disabled")

    def test_research_invalid_claim_recorded_as_gap(self):
        result = execute_pipeline({"topic": "Example", "research_items": [{"claim": "x"}]})
        item = result["stages"]["research"]["result"]["items"][0]
        self.assertTrue(item["validation_errors"])

    def test_learning_optional(self):
        result=execute_pipeline({"topic":"Example"})
        self.assertEqual(result["stages"]["learning_loop"]["status"],"not_executable")

    def test_invalid_topic(self):
        with self.assertRaises(ValueError):
            execute_pipeline({"topic": ""})

if __name__ == "__main__":
    unittest.main()
