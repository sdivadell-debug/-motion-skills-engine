import unittest
from youtube_agent.production_editor import build_edit_plan
from youtube_agent.shorts_cutter import shortlist_clips
from youtube_agent.seo import draft_metadata

class TestProductionShortsSEO(unittest.TestCase):
 def test_edit_plan(self):
  p=build_edit_plan([{"text":"Some content","start":2}])
  self.assertEqual(p["cues"][0]["start"],2)
 def test_invalid_segment(self):
  with self.assertRaises(ValueError): build_edit_plan([{}])
 def test_shortlist(self):
  s=shortlist_clips([{"text":"A short snippet"},{"text":"This is a longer segment with enough text to suggest possible clip selection."}])
  self.assertEqual(len(s),1)
 def test_seo_draft(self):
  m=draft_metadata("topic",["fact"],["keyword"])
  self.assertEqual(m["status"],"draft")
 def test_bad_seo_input(self):
  with self.assertRaises(ValueError): draft_metadata("topic",[1])

if __name__=="__main__": unittest.main()
