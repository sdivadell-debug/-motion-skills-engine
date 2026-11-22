"""Optional AI-assisted draft commands."""
import argparse
import json

from .ai_provider import generate_json, ProviderError
from .ai_prompts import script_prompt, ideas_prompt


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="command", required=True)
    s = sub.add_parser("script")
    s.add_argument("topic")
    s.add_argument("--audience", default="")
    s.add_argument("--angle", default="")
    s.add_argument("--evidence", default="[]")
    s.add_argument("--minutes", type=int, default=8)
    s.add_argument("--output")
    i = sub.add_parser("ideas")
    i.add_argument("niche")
    i.add_argument("--audience", default="")
    i.add_argument("--constraints", default="{}")
    i.add_argument("--output")
    a = p.parse_args()
    try:
        prompt = (script_prompt(a.topic, a.audience, a.angle, json.loads(a.evidence), a.minutes)
                  if a.command == "script" else ideas_prompt(a.niche, a.audience, json.loads(a.constraints)))
        result = generate_json(prompt)
        content = json.dumps(result, ensure_ascii=False, indent=2)
        if a.output:
            with open(a.output, "w", encoding="utf-8") as f:
                f.write(content + "\n")
        else:
            print(content)
    except (ProviderError, ValueError) as e:
        p.error(str(e))


if __name__ == "__main__":
    main()
