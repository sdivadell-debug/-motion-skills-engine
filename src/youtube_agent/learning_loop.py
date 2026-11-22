"""Capture observations and hypotheses from performance reviews."""
from __future__ import annotations__

def create_learning_record(observation: str, hypothesis: str, next_test: str, evidence: list[str] | None = None) -> dict:
    fields=(observation,hypothesis,next_test)
    if any(not isinstance(x,str) or not x.strip() for x in fields): raise ValueError("observation, hypothesis, and next_test are required")
    return {"observation":observation.strip(),"hypothesis":hypothesis.strip(),"next_test":next_test.strip(),"evidence":evidence or [],"status":"hypothesis_pending","warning":"Record is a hypothesis and does not establish causality."}
