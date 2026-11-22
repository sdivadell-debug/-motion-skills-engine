"""Lightweight deterministic helpers for chapters, hook variants, and comment triage."""
from __future__ import annotations
import re
from typing import Any

def generate_hook_variants(topic: str, audience: str = "") -> list[dict[str, str]]:
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("topic required")
    t=topic.strip()
    audience_clause=f" for {audience.strip()}" if audience.strip() else ""
    return [
      {"style":"question","hook":f"What do most people misunderstand about {t}?"},
      {"style":"promise","hook":f"By the end, you'll know how to approach {t} more clearly{audience_clause}."},
      {"style":"mistake","hook":f"The common mistake with {t} is easy to miss—and it can change the result."},
      {"style":"contrast","hook":f"There is a simpler way to think about {t} than the usual advice."},
      {"style":"story_setup","hook":f"I tested/ examined {t}; here's the key lesson. Replace this with a verified real example."},
    ]

def draft_chapters(segments: list[dict[str, Any]]) -> list[dict[str, str]]:
    if not isinstance(segments,list): raise ValueError("segments must be array")
    out=[]
    for i,s in enumerate(segments):
        if not isinstance(s,dict) or not isinstance(s.get("text"),str) or not s["text"].strip():
            raise ValueError(f"segment {i} needs text")
        start=s.get("start")
        if start is None: continue
        if not isinstance(start,(int,float)) or isinstance(start,bool) or start<0:
            raise ValueError(f"segment {i} start must be a nonnegative number")
        seconds=int(start)
        stamp=f"{seconds//3600:02d}:{(seconds%3600)//60:02d}:{seconds%60:02d}" if seconds>=3600 else f"{seconds//60:02d}:{seconds%60:02d}"
        title=re.sub(r"\s+"," ",s["text"].strip())
        title=title[:72].rstrip()
        out.append({"timestamp":stamp,"title":title,"source_segment":str(i)})
    return out

def classify_comment(comment: str) -> str:
    if not isinstance(comment,str): raise ValueError("comment must be string")
    text=comment.casefold()
    if any(term in text for term in ("scam","fraud","fake","lie")): return "possible_criticism"
    if any(term in text for term in ("how do","where can","what is","please explain")): return "question"
    if any(term in text for term in ("thank","great video","helpful","love this")): return "positive"
    return "unclassified"
