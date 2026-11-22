import json
import unittest
from unittest.mock import patch
from io import BytesIO

from youtube_agent.youtube_api import YouTubeDataAPI, YouTubeAPIError


class FakeResponse:
    def __init__(self, payload):
        self.payload = json.dumps(payload).encode()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False
    def read(self):
        return self.payload


class YouTubeApiTests(unittest.TestCase):
    def test_requires_api_key(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                YouTubeDataAPI()

    def test_collects_channel_upload_metrics(self):
        responses = [
            {"items":[{"id":{"channelId":"ch1"}}]},
            {"items":[{"id":"ch1","snippet":{"title":"Channel One"},"contentDetails":{"relatedPlaylists":{"uploads":"up1"}}}]},
            {"items":[{"contentDetails":{"videoId":"v1"}},{"contentDetails":{"videoId":"v2"}},{"contentDetails":{"videoId":"v3"}}]},
            {"items":[
                {"id":"v1","snippet":{"channelId":"ch1","title":"One","publishedAt":"2026-11-01T00:00:00Z"},"statistics":{"viewCount":"100"}},
                {"id":"v2","snippet":{"channelId":"ch1","title":"Two","publishedAt":"2026-11-02T00:00:00Z"},"statistics":{"viewCount":"200"}},
                {"id":"v3","snippet":{"channelId":"ch1","title":"Three","publishedAt":"2026-11-03T00:00:00Z"},"statistics":{}}
            ]}
        ]
        def fake_urlopen(*args, **kwargs):
            return FakeResponse(responses.pop(0))
        api = YouTubeDataAPI(api_key="test-key")
        with patch("youtube_agent.youtube_api.urlopen", side_effect=fake_urlopen):
            result = api.collect_competitor_videos("woodworking", 1, 3)
        self.assertEqual(len(result["videos"]), 2)
        self.assertEqual(result["skipped_private_metrics"], 1)
        self.assertEqual(result["videos"][0]["views"], 100)
        self.assertEqual(result["videos"][0]["data_source"], "YouTube Data API v3")

    def test_rejects_too_few_videos_for_baseline(self):
        api = YouTubeDataAPI(api_key="test-key")
        with self.assertRaises(ValueError):
            api.collect_competitor_videos("topic", 1, 2)

    def test_api_error_is_surfaced(self):
        api = YouTubeDataAPI(api_key="test-key")
        with patch("youtube_agent.youtube_api.urlopen", return_value=FakeResponse({"error":{"errors":[{"reason":"quotaExceeded"}]}})):
            with self.assertRaises(YouTubeAPIError):
                api._get("search", part="snippet")


if __name__ == "__main__":
    unittest.main()
