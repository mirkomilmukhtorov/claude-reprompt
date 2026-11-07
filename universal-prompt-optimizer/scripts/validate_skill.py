#!/usr/bin/env python3
from pathlib import Path
p=Path(__file__).resolve().parents[1]
s=(p/"SKILL.md").read_text()
assert s.startswith("---\n") and "name: universal-prompt-optimizer" in s
for part in ["data/models.json","references/reasoning-modes.md","references/openai-prompting.md","references/gemini-prompting.md","references/claude-prompting.md","scripts/optimizer.py"]:
    assert (p/part).is_file(),part
print("Skill structure valid.")
