import json
import unittest
from unittest.mock import patch

from youtube_agent.analytics import analyze_performance
from youtube_agent.youtube_analytics_api import (
    query_report, fetch_video_retention, YouTubeAnalyticsError,
)


class AnalyticsTests(unittest.TestCase):
    def test_comparisons_are_separated_by_format_and_age(self):
        rows = [
            {"title": "Long A", "views": 100, "format": "long_form", "age_window_days": 7},
            {"title": "Long B", "views": 200, "format": "long_form", "age_window_days": 7},
            {"title": "Long C", "views": 300, "format": "long_form", "age_window_days": 7},
            {"title": "Short A", "views": 900, "format": "shorts", "age_window_days": 7},
            {"title": "Short B", "views": 1000, "format": "shorts", "age_window_days": 7},
            {"title": "Short C", "views": 1100, "format": "shorts", "age_window_days": 7},
        ]
        result = analyze_performance(rows)
        long_a = next(v for v in result["videos"] if v["title"] == "Long A")
        short_a = next(v for v in result["videos"] if v["title"] == "Short A")
        self.assertEqual(long_a["comparisons"]["views"]["cohort_median"], 200)
        self.assertEqual(short_a["comparisons"]["views"]["cohort_median"], 1000)

    def test_small_cohort_is_not_overinterpreted(self):
        result = analyze_performance([{"title": "One", "views": 50, "format": "shorts"}])
        self.assertFalse(result["videos"][0]["cohort_comparable"])
        self.assertIsNone(result["videos"][0]["views_vs_median"])

    def test_optional_metrics_and_missing_data(self):
        result = analyze_performance([
            {"title": "A", "views": 100, "ctr": 4.2, "average_view_percentage": 45},
            {"title": "B", "views": 120, "ctr": 5.1, "average_view_percentage": 50},
            {"title": "C", "views": 90, "ctr": 3.8, "average_view_percentage": 40},
        ])
        self.assertIn("ctr", result["cohort_baselines"][0]["metrics"])
        self.assertIn("impressions", result["videos"][0]["missing_metrics"])

    def test_invalid_ctr_is_rejected(self):
        with self.assertRaises(ValueError):
            analyze_performance([{"title": "Bad", "views": 20, "ctr": 150}])

    def test_invalid_video_input_is_rejected(self):
        with self.assertRaises(ValueError):
            analyze_performance([{"views": 20}])

    def test_views_are_required(self):
        with self.assertRaises(ValueError):
            analyze_performance([{"title": "No views"}])


class YouTubeAnalyticsApiTests(unittest.TestCase):
    @patch("youtube_agent.youtube_analytics_api.urlopen")
    def test_report_rows_are_mapped_using_column_headers(self, mock_urlopen):
        class Response:
            def __enter__(self): return self
            def __exit__(self, *args): return False
            def read(self):
                return json.dumps({
                    "columnHeaders": [{"name": "video"}, {"name": "views"}],
                    "rows": [["abc123", 42]],
                }).encode()
        mock_urlopen.return_value = Response()
        result = query_report("token", "2026-01-01", "2026-01-07", ["views"], ["video"])
        self.assertEqual(result["rows"], [{"video": "abc123", "views": 42}])
        request = mock_urlopen.call_args.args[0]
        self.assertEqual(request.get_header("Authorization"), "Bearer token")

    def test_rejects_write_or_monetary_metric(self):
        with self.assertRaises(ValueError):
            query_report("token", "2026-01-01", "2026-01-07", ["estimatedRevenue"])

    def test_retention_requires_one_video_id(self):
        with self.assertRaises(ValueError):
            fetch_video_retention("token", "bad id", "2026-01-01", "2026-01-07")


if __name__ == "__main__":
    unittest.main()
