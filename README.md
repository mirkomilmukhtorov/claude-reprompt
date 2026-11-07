# Universal Prompt Optimizer

This repository supersedes Claude Reprompt with a model-aware prompt rewriting and routing skill for OpenAI, Gemini and Claude. The original /claude-reprompt command remains available as a compatibility alias; new installations should use /universal-prompt-optimizer.

## Install on macOS (all supported agents)

Run from Terminal:

1. git clone https://github.com/mirkomilmukhtorov/claude-reprompt.git ~/Downloads/claude-reprompt-universal
2. sh ~/Downloads/claude-reprompt-universal/universal-prompt-optimizer/scripts/install_all.sh

The script installs to ~/.agents/skills (Codex and Gemini CLI), ~/.claude/skills (Claude Code), and ~/.gemini/config/skills (Antigravity). It backs up an existing claude-reprompt directory rather than deleting it, and refuses to overwrite an existing universal-prompt-optimizer installation.

Alternatively, where compatible with your installed skills CLI:

npx skills add mirkomilmukhtorov/claude-reprompt --skill universal-prompt-optimizer --global --yes

## Use

Ask: /universal-prompt-optimizer Rewrite this prompt for the best model, tell me its supported reasoning level, and preserve every requirement: ...

Or run: python3 universal-prompt-optimizer/scripts/optimizer.py --prompt 'Audit my repository read-only'

The Python script is an offline baseline router, not a substitute for an LLM semantic rewrite.

## Verification

python3 universal-prompt-optimizer/scripts/validate_registry.py
python3 universal-prompt-optimizer/scripts/validate_skill.py

## Limitations

Dated registry: November 7, 2026. Reverify model availability, API IDs, reasoning support and pricing against official sources before relying on them. This source repository is a GitHub-compatible distribution; the separate full ZIP archive from the original creation session contains additional static benchmarks and development tests. Installation on a user's physical Mac cannot be verified by GitHub updates.
