import unittest

from youtube_agent.orchestrator import WorkflowRun, create_workflow_plan, WORKFLOW


class OrchestratorTests(unittest.TestCase):
    def test_plan_contains_all_stages_and_approval(self):
        plan = create_workflow_plan("Build a shed")
        self.assertEqual([s["name"] for s in plan["workflow"]], WORKFLOW)
        self.assertTrue(plan["approval_required"])
        self.assertEqual(plan["status"], "planned")

    def test_profile_is_included(self):
        profile = {"channel_name": "Test"}
        plan = create_workflow_plan("Topic", profile)
        self.assertEqual(plan["profile"], profile)
        self.assertEqual(plan["workflow"][0]["input"]["profile"], profile)

    def test_rejects_empty_topic(self):
        with self.assertRaises(ValueError):
            WorkflowRun("  ")

    def test_stage_status_update(self):
        run = WorkflowRun("topic")
        stage = run.mark_stage("research", "complete", {"sources": 2})
        self.assertEqual(stage["status"], "complete")
        self.assertEqual(stage["output"], {"sources": 2})

    def test_rejects_invalid_stage(self):
        run = WorkflowRun("topic")
        with self.assertRaises(ValueError):
            run.mark_stage("not-a-stage", "complete")

    def test_rejects_invalid_status(self):
        run = WorkflowRun("topic")
        with self.assertRaises(ValueError):
            run.mark_stage("research", "failed")


if __name__ == "__main__":
    unittest.main()
