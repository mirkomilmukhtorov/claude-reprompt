#!/usr/bin/env python3
"""Offline, transparent prompt-router scaffold (not an LLM rewriter)."""
import argparse
import json
from pathlib import Path
import re

REGISTRY = Path(__file__).resolve().parents[1] / "data" / "models.json"

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--provider", choices=["openai","google","anthropic"])
    ap.add_argument("--model")
    ap.add_argument("--mode", default="auto", choices=["auto","universal","specific","cross","quality","efficient","coding","research","multi-agent","diagnose"])
    args = ap.parse_args()
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    models = [m for m in data["models"] if m["status"] == "active_at_snapshot"]
    p = args.prompt.lower()
    hard = bool(re.search(r"\b(architecture|complex|security|multi-file|production|debug|audit|proof|research|migration)\b", p))
    coding = bool(re.search(r"\b(code|debug|repository|test|api|typescript|python|deploy|refactor|bug)\b", p))
    research = bool(re.search(r"\b(research|sources|citations|investigate|verify)\b", p))
    if args.model:
        chosen = next((x for x in models if x["id"] == args.model or x["name"].lower() == args.model.lower()), None)
        if chosen is None:
            ap.error("Requested model is not in the verified snapshot; recheck provider documentation.")
    else:
        if args.provider == "google":
            ident = "gemini-4-argon" if hard else "gemini-3.8-flash" if coding or research else "gemini-3.5-flash-lite"
        elif args.provider == "anthropic":
            ident = "claude-opus-5-5" if hard else "claude-sonnet-5-5" if coding or research else "claude-haiku-5-5"
        elif args.provider == "openai":
            ident = "gpt-6-astra" if hard else "gpt-6.1-sol" if coding or research else "gpt-6-luna"
        else:
            ident = "claude-opus-5-5" if hard and coding else "gpt-6-astra" if hard else "gpt-6.1-sol" if coding or research else "gpt-6-luna"
        chosen = next(x for x in models if x["id"] == ident)
    supported = chosen["reasoning"]["supported"]
    level = "high" if hard or args.mode == "quality" else "medium" if coding or research else "minimal" if "minimal" in supported else "low" if "low" in supported else supported[0]
    if level not in supported:
        level = supported[-1] if hard else supported[0]
    result = {
        "mode": args.mode,
        "model": chosen["id"],
        "provider": chosen["provider"],
        "reasoning_parameter": chosen["reasoning"]["parameter"],
        "reasoning_value": level,
        "registry_verified_on": data["verified_on"],
        "scope_notice": "This is an offline rules-based scaffold, not a semantic LLM rewrite or live model availability check.",
        "prompt_scaffold": "Objective: " + args.prompt.strip() + "\n\nPreserve the stated scope and constraints. Clarify assumptions, required inputs, deliverable, tools and acceptance criteria. Verify factual claims and report blockers without inventing results."
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
