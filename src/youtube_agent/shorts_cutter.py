"""Identify transcript passages that may work as short-form clips."""
from __future__ import annotations

def shortlist_clips(segments: list[dict], max_clips: int = 5) -> list[dict]:
    if not isinstance(segments,list): raise ValueError("segments must be an array")
    if isinstance(max_clips,bool) or not isinstance(max_clips,int) or max_clips<1: raise ValueError("max_clips must be positive")
    candidates=[]
    for i,s in enumerate(segments):
        if not isinstance(s,dict) or not isinstance(s.get("text"),str): raise ValueError(f"segment {i} needs text")
        txt=s["text"].strip()
        if not txt: continue
        # Transparent length heuristic only, not semantic prediction.
        if len(txt)>=60:
            candidates.append({"segment":i,"text":txt,"start":s.get("start"),"end":s.get("end"),"reason":"Passage length may support a standalone excerpt; human review required."})
    return candidates[:max_clips]
