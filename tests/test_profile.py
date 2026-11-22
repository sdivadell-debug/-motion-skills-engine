import unittest

from youtube_agent.profile import validate_channel_profile


class ChannelProfileTests(unittest.TestCase):
    def valid_profile(self):
        return {
            "channel_name": "Test Channel",
            "niche": "Home improvement",
            "primary_audience": "DIY beginners",
            "language": "en",
            "voice": {"tone": "clear and practical"},
            "content_pillars": ["tutorials"],
            "performance_baseline": {
                "source": "YouTube Studio export",
                "period_start": "2026-10-01",
                "period_end": "2026-10-31",
                "metrics": {"views": 1200, "ctr": 4.2}
            }
        }

    def test_accepts_valid_profile(self):
        self.assertEqual(validate_channel_profile(self.valid_profile()), [])

    def test_reports_missing_required_fields(self):
        errors = validate_channel_profile({"channel_name": "Only name"})
        self.assertTrue(any("niche" in error for error in errors))
        self.assertTrue(any("voice" in error for error in errors))

    def test_rejects_negative_capacity(self):
        profile = self.valid_profile()
        profile["publishing_capacity_per_week"] = -1
        self.assertIn("publishing_capacity_per_week must be a non-negative number",
                      validate_channel_profile(profile))

    def test_rejects_reversed_baseline_dates(self):
        profile = self.valid_profile()
        profile["performance_baseline"]["period_start"] = "2026-11-30"
        profile["performance_baseline"]["period_end"] = "2026-11-01"
        self.assertIn("performance_baseline.period_start must not be after period_end",
                      validate_channel_profile(profile))

    def test_rejects_unknown_fields(self):
        profile = self.valid_profile()
        profile["subscriber_guess"] = 10000
        self.assertIn("unknown field: subscriber_guess", validate_channel_profile(profile))


if __name__ == "__main__":
    unittest.main()
