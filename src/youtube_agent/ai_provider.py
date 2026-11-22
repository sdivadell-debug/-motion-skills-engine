"""Optional OpenAI-compatible AI provider; secrets are read from environment only."""
from __future__ import annotations

import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class ProviderError(RuntimeError):
    """Safe, user-facing error for provider configuration or responses."""


def generate_json(prompt: str, *, model: str | None = None) -> dict:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ProviderError("OPENAI_API_KEY is not configured.")

    endpoint = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1").rstrip("/") + "/chat/completions"
    model = model or os.environ.get("YOUTUBE_AGENT_MODEL", "gpt-4o-mini")
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Return valid JSON only. Do not invent sources or claim actions you did not perform."},
            {"role": "user", "content": prompt},
        ],
        "response_format": {"type": "json_object"},
    }
    req = Request(
        endpoint,
        data=json.dumps(payload).encode(),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
        data = json.loads(raw)
    except (HTTPError, URLError, TimeoutError, OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ProviderError("Provider request failed or returned unreadable data.") from exc

    try:
        message = data["choices"][0]["message"]["content"]
        result = json.loads(message)
        if not isinstance(result, dict):
            raise TypeError("JSON response must be an object")
        return result
    except (KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        raise ProviderError("Provider response was not a valid JSON object.") from exc
