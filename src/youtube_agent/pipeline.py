"""Offline orchestrated workflow for implemented YouTube pipeline components."""
from __future__ import annotations
from typing import Any
from .profile import validate_channel_profile
from .research import research_brief
from .outliers import analyze_outliers
from .idea_scoring import Idea, rank_ideas
from .script_studio import build_script
from .packaging import create_packaging_brief
from .production_editor import build_edit_plan
from .shorts_cutter import shortlist_clips
from .seo import draft_metadata
from .analytics import analyze_performance
from .learning_loop import create_learning_record
from .community import classify_comments
from .weekly_planner import build_week_plan
from .ai_prompts import pipeline_review_prompt
from .ai_provider import generate_json, ProviderError

HANDLERS = {
 "channel_profile": lambda d: {"errors":validate_channel_profile(d.get("profile",{})),"valid":not validate_channel_profile(d.get("profile",{}))},
 "research": lambda d: research_brief(d.get("topic",""),d.get("research_items",[])),
 "competitor_research":lambda d:{"results":analyze_outliers(d.get("competitor_videos",[])),"notice":"Supplied data only; no live discovery."},
 "idea_lab":lambda d:{"ranked_ideas":rank_ideas([Idea(**i) for i in d.get("ideas",[])])},
 "script_studio":lambda d:build_script(d["topic"],d.get("audience",""),d.get("angle",""),d.get("research_items",[]),d.get("duration_minutes",8)),
 "packaging":lambda d:create_packaging_brief(d["topic"],d.get("angle",""),d.get("audience","")),
 "production_editor":lambda d:build_edit_plan(d.get("transcript_segments",[])),
 "shorts_cutter":lambda d:{"candidate_clips":shortlist_clips(d.get("transcript_segments",[]))},
 "seo_publisher":lambda d:draft_metadata(d["topic"],d.get("description_facts",[]),d.get("keywords",[])),
 "analytics":lambda d:analyze_performance(d.get("performance_videos",[])),
 "learning_loop":lambda d:create_learning_record(d["observation"],d["hypothesis"],d["next_test"],d.get("evidence",[])),
 "community":lambda d:classify_comments(d.get("comments",[])),
 "weekly_planner":lambda d:build_week_plan(d.get("tasks",[]),d.get("weekly_capacity",5)),
}

def execute_pipeline(payload:dict[str,Any])->dict[str,Any]:
 if not isinstance(payload,dict): raise ValueError("input payload must be a JSON object")
 topic=payload.get("topic")
 if not isinstance(topic,str) or not topic.strip(): raise ValueError("topic must be a non-empty string")
 stages={}
 ordered=("channel_profile","research","competitor_research","idea_lab","script_studio","packaging","production_editor","shorts_cutter","seo_publisher","analytics","learning_loop","community","weekly_planner")
 for name in ordered:
  handler=HANDLERS[name]
  try:
   # Learning record is opt-in: avoid blocking when user has no hypothesis yet.
   if name=="learning_loop" and not all(k in payload for k in ("observation","hypothesis","next_test")):
    stages[name]={"status":"not_executable","note":"Provide observation, hypothesis, and next_test to activate."}
    continue
   stages[name]={"status":"complete","result":handler(payload)}
  except (ValueError,TypeError,KeyError) as exc:
   stages[name]={"status":"blocked","error":str(exc)}
 if payload.get("ai_review") is True:
  try:
   review_input={"topic":topic,"stages":stages}
   stages["ai_review"]={"status":"complete","result":generate_json(pipeline_review_prompt(review_input))}
  except ProviderError as exc:
   stages["ai_review"]={"status":"blocked","error":str(exc)}
 stages["creator_review"]={"status":"approval_required","note":"Human review is required before external side effects."}
 return {"topic":topic,"stages":stages,"external_actions":"disabled","approval_required":True,"publishing":"disabled"}
