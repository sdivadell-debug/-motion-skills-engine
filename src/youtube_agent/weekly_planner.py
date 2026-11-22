"""Capacity-aware weekly planning from user-provided priorities."""
from __future__ import annotations

def build_week_plan(tasks: list[dict], capacity: int = 5) -> dict:
    if not isinstance(tasks,list): raise ValueError("tasks must be array")
    if isinstance(capacity,bool) or not isinstance(capacity,int) or capacity<1: raise ValueError("capacity must be positive integer")
    validated=[]
    for i,t in enumerate(tasks):
        if not isinstance(t,dict) or not isinstance(t.get("name"),str) or not t["name"].strip(): raise ValueError(f"task {i} needs name")
        weight=t.get("priority",1)
        if isinstance(weight,bool) or not isinstance(weight,(int,float)) or weight<=0: raise ValueError("priority must be positive")
        validated.append(dict(t))
    sorted_tasks=sorted(validated,key=lambda t:t.get("priority",1),reverse=True)
    return {"capacity":capacity,"scheduled":sorted_tasks[:capacity],"deferred":sorted_tasks[capacity:],"warning":"Priority ranking is heuristic; schedule and workload require human review."}
