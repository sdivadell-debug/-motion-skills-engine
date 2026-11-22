"""Structured script draft builder; deterministic template, not an LLM."""
from __future__ import annotations
from typing import Any

def build_script(topic: str, audience: str = "", angle: str = "", evidence: list[dict[str, Any]] | None = None, duration_minutes: int = 8) -> dict[str, Any]:
    if not isinstance(topic,str) or not topic.strip(): raise ValueError("topic required")
    if isinstance(duration_minutes,bool) or not isinstance(duration_minutes,int) or not 1 <= duration_minutes <= 60: raise ValueError("duration_minutes must be 1-60")
    evidence=evidence or []
    return {
      "topic":topic.strip(),"audience":audience,"angle":angle,"target_duration_minutes":duration_minutes,
      "status":"template_draft","disclaimer":"Template structure only; not a generated researched script. Replace placeholders and verify claims.",
      "sections":[
        {"name":"hook","target_seconds":20,"prompt":"Open with a compelling question, contrast, surprising fact, or clear promise. Verify factual claims."},
        {"name":"promise_and_context","target_seconds":30,"prompt":"Explain what the viewer will gain and why the topic matters."},
        {"name":"main_point_1","prompt":"Explain the first core idea with an example and source-backed claims."},
        {"name":"main_point_2","prompt":"Explain the second core idea; use demonstration, contrast, or evidence."},
        {"name":"main_point_3","prompt":"Explain the third core idea; address common misconceptions or limitations."},
        {"name":"summary","target_seconds":30,"prompt":"Summarize the useful takeaways without repeating the entire video."},
        {"name":"call_to_action","target_seconds":15,"prompt":"Use a relevant, non-manipulative CTA."}],
      "evidence":evidence,"evidence_warning":"Evidence items must be reviewed; the template does not verify sources or create citations."
    }
