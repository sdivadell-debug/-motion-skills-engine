import unittest

from youtube_agent.outliers import analyze_outliers


def video(video_id, views):
    return {
        "video_id": video_id,
        "channel_id": "channel-a",
        "views": views,
        "source_url": f"https://youtube.com/watch?v={video_id}",
        "retrieved_at": "2026-11-22",
    }


class OutlierTests(unittest.TestCase):
    def test_uses_same_channel_leave_one_out_median(self):
        rows = analyze_outliers([video("a", 100), video("b", 120), video("c", 900), video("d", 110)])
        standout = next(row for row in rows if row["video_id"] == "c")
        self.assertEqual(standout["baseline_median_views"], 110)
        self.assertAlmostEqual(standout["views_multiple"], 900 / 110)
        self.assertTrue(standout["is_outlier"])

    def test_requires_three_videos_for_leave_one_out_baseline(self):
        self.assertEqual(analyze_outliers([video("a", 10), video("b", 20)]), [])

    def test_rejects_missing_source(self):
        item = video("a", 10)
        del item["source_url"]
        with self.assertRaises(ValueError):
            analyze_outliers([item])

    def test_rejects_negative_views(self):
        with self.assertRaises(ValueError):
            analyze_outliers([video("a", -1)])

    def test_rejects_duplicate_video(self):
        with self.assertRaises(ValueError):
            analyze_outliers([video("a", 10), video("a", 20)])

    def test_rejects_invalid_threshold(self):
        with self.assertRaises(ValueError):
            analyze_outliers([], threshold=0)

    def test_zero_baseline_stays_valid_json(self):
        rows = analyze_outliers([video("a", 0), video("b", 0), video("c", 25)])
        standout = next(row for row in rows if row["video_id"] == "c")
        self.assertIsNone(standout["views_multiple"])
        self.assertTrue(standout["baseline_zero"])
        self.assertTrue(standout["is_outlier"])

    def test_rejects_invalid_retrieval_date(self):
        item = video("a", 10)
        item["retrieved_at"] = "not-a-date"
        with self.assertRaises(ValueError):
            analyze_outliers([item])


if __name__ == "__main__":
    unittest.main()
