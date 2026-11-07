#!/bin/sh
# Install the source in Codex, Claude Code, Gemini CLI and Antigravity.
# Preserves any previous installation by renaming it to a timestamped backup.
set -eu
SKILL_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
NAME=universal-prompt-optimizer
STAMP=$(date +%Y%m%d-%H%M%S)
for ROOT in "$HOME/.agents/skills" "$HOME/.claude/skills" "$HOME/.gemini/config/skills"; do
  mkdir -p "$ROOT"
  if [ -d "$ROOT/claude-reprompt" ] && [ ! -L "$ROOT/claude-reprompt" ]; then
    mv "$ROOT/claude-reprompt" "$ROOT/claude-reprompt.backup-$STAMP"
  fi
  if [ -e "$ROOT/$NAME" ] || [ -L "$ROOT/$NAME" ]; then
    echo "Existing target preserved, install manually after comparison: $ROOT/$NAME" >&2
    continue
  fi
  cp -R "$SKILL_DIR" "$ROOT/$NAME"
  echo "INSTALLED: $ROOT/$NAME"
done
echo "Restart Codex, Claude Code, Gemini CLI, and Antigravity."
