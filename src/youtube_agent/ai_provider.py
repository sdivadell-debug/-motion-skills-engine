"""Optional OpenAI-compatible AI provider; secrets are read from environment only."""
from __future__ import annotations
import json, os
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

class ProviderError(RuntimeError): pass

def generate_json(prompt: str, *, model: str | None = None) -> dict:
    key=os.environ.get("OPENAI_API_KEY")
    if not key: raise ProviderError("OPENAI_API_KEY is not configured.")
    endpoint=os.environ.get("OPENAI_API_BASE","https://api.openai.com/v1").rstrip("/")+"/chat/completions"
    model=model or os.environ.get("YOUTUBE_AGENT_MODEL","gpt-4o-mini")
    payload={"model":model,"messages":[{"role":"system","content":"Return valid JSON only. Do not invent sources or claim actions you did not perform."},{"role":"user","content":prompt}],"response_format":{"type":"json_object"}}
    req=Request(endpoint,data=json.dumps(payload).encode(),headers={"Authorization":"Bearer "+key,"Content-Type":"application/json"},method="POST")
    try:
        with urlopen(req,timeout=60) as resp: data=json.loads(resp.read().decode())
    except (HTTPError,URLError,TimeoutError) as exc: raise ProviderError(f"Provider request failed: {exc}") from exc
    try: return json.loads(data["choices"][0]["message"]["content"])
    except (KeyError,IndexError,TypeError,json.JSONDecodeError) as exc: raise ProviderError("Provider response was not valid JSON.") from exc
