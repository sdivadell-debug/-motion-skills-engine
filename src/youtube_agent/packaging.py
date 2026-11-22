"""Packaging brief templates for titles and thumbnails."""
from __future__ import annotations

def create_packaging_brief(topic: str, angle: str = "", audience: str = "") -> dict:
    if not isinstance(topic,str) or not topic.strip(): raise ValueError("topic required")
    return {"topic":topic,"angle":angle,"audience":audience,"status":"creative_brief_template",
      "warning":"Suggestions below are prompts for human/AI creative development, not completed title or image assets.",
      "title_directions":[
       {"approach":"specific outcome","prompt":"State a concrete viewer outcome without exaggerating."},
       {"approach":"curiosity gap","prompt":"Create curiosity that the video genuinely resolves; avoid misleading claims."},
       {"approach":"contrarian insight","prompt":"Challenge a familiar assumption only if the content substantiates it."},
       {"approach":"practical guide","prompt":"Make the scope and usefulness clear."}],
      "thumbnail_directions":[
       {"concept":"single visual focal point","prompt":"One clear subject or object; readable on mobile."},
       {"concept":"before versus after","prompt":"Use only when the video honestly demonstrates the contrast."},
       {"concept":"visual metaphor","prompt":"Represent the core idea with one recognizable visual metaphor."}],
      "checklist":["Title and thumbnail make the same promise.","No false urgency or fabricated result.","Thumbnail remains legible at small size.","The script delivers the promise."]}
