import unittest
from youtube_agent.analytics import analyze_performance
from youtube_agent.learning_loop import create_learning_record
from youtube_agent.community import classify_comments
from youtube_agent.weekly_planner import build_week_plan

class TestExtensions(unittest.TestCase):
 def test_metrics(self):
  a=analyze_performance([{"title":"a","views":100},{"title":"b","views":300}])
  self.assertEqual(a["median_views"],200)
 def test_learning_record(self):
  r=create_learning_record("CTR low","title may be unclear","test a clearer title")
  self.assertEqual(r["status"],"hypothesis_pending")
 def test_comment_review(self):
  r=classify_comments([{"text":"hello"}])
  self.assertEqual(r[0]["status"],"needs_human_review")
 def test_week_planner(self):
  r=build_week_plan([{"name":"a","priority":3},{"name":"b","priority":1}],1)
  self.assertEqual(len(r["scheduled"]),1)
  self.assertEqual(len(r["deferred"]),1)
 def test_invalid_metrics(self):
  with self.assertRaises(ValueError): analyze_performance([{"title":"x","views":-1}])

if __name__=="__main__":unittest.main()
