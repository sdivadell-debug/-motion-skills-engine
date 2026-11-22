import unittest
from youtube_agent.ai_prompts import script_prompt,ideas_prompt
class TestAIPrompts(unittest.TestCase):
 def test_script_prompt_has_topic(self): self.assertIn("Test topic",script_prompt("Test topic","audience","angle",[]))
 def test_ideas_prompt(self): self.assertIn("10 distinct",ideas_prompt("niche","audience"))
if __name__=="__main__": unittest.main()
