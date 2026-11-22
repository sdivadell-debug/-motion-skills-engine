"""Create editor decision cues from user-provided transcript segments."""
from __future__ import annotations

def build_edit_plan(segments: list[dict]) -> dict:
    if not isinstance(segments,list): raise ValueError("segments must be an array")
    cues=[]
    for i,s in enumerate(segments):
        if not isinstance(s,dict) or not isinstance(s.get("text"),str) or not s["text"].strip():
            raise ValueError(f"segment {i} must contain text")
        cue={"segment":i,"text":s["text"],"suggested_visual":"Consider illustrative B-roll, on-screen text, or a demonstration relevant to this passage."}
        if "start" in s: cue["start"]=s["start"]
        if "end" in s: cue["end"]=s["end"]
        cues.append(cue)
    return {"status":"edit_plan","cues":cues,"warning":"Suggestions only; no video/audio files edited."}
