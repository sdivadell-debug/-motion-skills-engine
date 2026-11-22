"""Analyze supplied video performance metrics with simple transparent comparisons."""
from __future__ import annotations
from statistics import median

def analyze_performance(videos: list[dict]) -> dict:
    if not isinstance(videos,list): raise ValueError("videos must be an array")
    checked=[]
    for i,v in enumerate(videos):
        if not isinstance(v,dict): raise ValueError(f"video {i} must be object")
        for key in ("title","views"):
            if key not in v: raise ValueError(f"video {i} missing {key}")
        views=v["views"]
        if isinstance(views,bool) or not isinstance(views,(int,float)) or views<0: raise ValueError("views must be nonnegative number")
        checked.append(dict(v))
    if not checked: return {"video_count":0,"median_views":None,"videos":[],"notes":"No data supplied."}
    baseline=median(v["views"] for v in checked)
    for v in checked:
        v["views_vs_median"]=None if baseline==0 else round(v["views"]/baseline,2)
    return {"video_count":len(checked),"median_views":baseline,"videos":checked,"notes":"Descriptive comparison only. Views are not a causal measure of quality."}
