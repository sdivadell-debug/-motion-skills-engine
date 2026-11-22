"""Draft metadata fields from user-supplied facts, avoiding invented claims."""
from __future__ import annotations

def draft_metadata(topic: str, description_facts: list[str] | None = None, keywords: list[str] | None = None) -> dict:
    if not isinstance(topic,str) or not topic.strip(): raise ValueError("topic required")
    facts=description_facts or []
    if any(not isinstance(f,str) for f in facts): raise ValueError("description_facts must be strings")
    kws=keywords or []
    if any(not isinstance(k,str) for k in kws): raise ValueError("keywords must be strings")
    description="\n".join(f"- {f}" for f in facts)
    return {"topic":topic.strip(),"title_placeholder":topic.strip(),"description_draft":description,"keywords":kws,"tags_note":"Tags/keywords are supplied inputs; relevance must be reviewed.","status":"draft","warning":"Metadata draft only; no claim about ranking or discoverability."}
