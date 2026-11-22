import unittest
from youtube_agent.script_studio import build_script
from youtube_agent.packaging import create_packaging_brief

class ScriptTests(unittest.TestCase):
 def test_script_template(self):
  out=build_script("topic",duration_minutes=5)
  self.assertEqual(out["status"],"template_draft")
  self.assertTrue(out["sections"])
 def test_invalid_duration(self):
  with self.assertRaises(ValueError): build_script("topic",duration_minutes=0)
 def test_package_brief(self):
  out=create_packaging_brief("topic")
  self.assertEqual(out["status"],"creative_brief_template")
  self.assertTrue(out["checklist"])
 def test_invalid_package(self):
  with self.assertRaises(ValueError): create_packaging_brief(" ")

if __name__=="__main__": unittest.main()
