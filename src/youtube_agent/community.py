"""Draft moderation/reply decisions from user-supplied comment records."""
from __future__ import annotations__

def classify_comments(comments: list[dict]) -> list[dict]:
    if not isinstance(comments,list): raise ValueError("comments must be array")
    out=[]
    for i,c in enumerate(comments):
        if not isinstance(c,dict) or not isinstance(c.get("text"),str): raise ValueError(f"comment {i} requires text")
        # No automated posting or moderation action: neutral review classification.
        out.append({"comment":c["text"],"author":c.get("author"),"status":"needs_human_review","suggested_category":"unclassified","reply_draft":None})
    return out
