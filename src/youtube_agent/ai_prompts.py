"""Prompt templates for AI-assisted content workflows."""
import json

def script_prompt(topic: str, audience: str, angle: str, evidence: list, duration_minutes: int=8) -> str:
    return ("Create a YouTube spoken-script draft as JSON with keys hook, outline, full_script, claims_to_verify, CTA. "
      "Use clear spoken language and label unsupported claims. Do not fabricate citations.\n"+json.dumps({"topic":topic,"audience":audience,"angle":angle,"evidence":evidence,"duration_minutes":duration_minutes},ensure_ascii=False))

def ideas_prompt(niche: str, audience: str, constraints: dict | None=None) -> str:
    return ("Generate 10 distinct YouTube video ideas as JSON {ideas:[{title,angle,audience_problem,proof_needed,production_cost}]}. "
      "Avoid asserting trend or demand without evidence.\n"+json.dumps({"niche":niche,"audience":audience,"constraints":constraints or {}},ensure_ascii=False))
