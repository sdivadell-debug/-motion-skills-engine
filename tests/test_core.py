import unittest

from youtube_agent.idea_scoring import Idea, score_idea, rank_ideas
from youtube_agent.research import validate_research_item, research_brief


class IdeaScoringTests(unittest.TestCase):
    def test_score_is_weighted_and_scaled(self):
        idea = Idea("A useful video", 10, 8, 6, 8, 10, ["https://example.com/a"])
        result = score_idea(idea)
        self.assertEqual(result["score"], 84.0)
        self.assertEqual(result["evidence_status"], "sourced")

    def test_invalid_score_is_rejected(self):
        idea = Idea("Bad input", 11, 5, 5, 5, 5, [])
        with self.assertRaises(ValueError):
            score_idea(idea)

    def test_missing_sources_are_not_hidden(self):
        idea = Idea("Unverified trend", 8, 8, 8, 8, 8, [])
        result = score_idea(idea)
        self.assertEqual(result["evidence_status"], "unsupported")
        self.assertEqual(result["confidence"], "low")

    def test_rank_orders_highest_first(self):
        low = Idea("Low", 2, 2, 2, 2, 2, [])
        high = Idea("High", 9, 9, 9, 9, 9, ["https://a.example", "https://b.example"])
        self.assertEqual(rank_ideas([low, high])[0]["title"], "High")


class ResearchValidationTests(unittest.TestCase):
    def test_sourced_claim_requires_url_and_date(self):
        errors = validate_research_item({
            "claim": "A trend is growing",
            "evidence_type": "sourced"
        })
        self.assertTrue(any("source_url" in error for error in errors))
        self.assertTrue(any("retrieved_at" in error for error in errors))

    def test_valid_sourced_claim(self):
        errors = validate_research_item({
            "claim": "A sourced observation",
            "evidence_type": "sourced",
            "source_url": "https://example.com/report",
            "retrieved_at": "2026-11-22"
        })
        self.assertEqual(errors, [])

    def test_measured_claim_requires_origin(self):
        errors = validate_research_item({
            "claim": "CTR is 5.2%",
            "evidence_type": "measured"
        })
        self.assertIn("measured claims require metric_origin", errors)


if __name__ == "__main__":
    unittest.main()
