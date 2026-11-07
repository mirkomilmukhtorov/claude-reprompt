#!/bin/sh
# Install Universal Prompt Optimizer globally for Codex, Claude Code, Gemini CLI,
# and Antigravity; bridge the Skills CLI's Antigravity path to the current
# Antigravity App's global skill discovery directory.
set -eu

if ! command -v npx >/dev/null 2>&1; then
  echo "npx is required. Install a compatible Node.js release first." >&2
  exit 1
fi
if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync is required for the Antigravity compatibility copy." >&2
  exit 1
fi

npx skills add mirkomilmukhtorov/claude-reprompt \
  --skill universal-prompt-optimizer \
  --global \
  --agent codex \
  --agent claude-code \
  --agent gemini-cli \
  --agent antigravity \
  --yes

NAME=universal-prompt-optimizer
TARGET="$HOME/.gemini/config/skills/$NAME"

# Google documents ~/.gemini/config/skills for Antigravity App.
# Current Skills CLI documents ~/.gemini/antigravity/skills for --agent antigravity.
SOURCE=""
for candidate in \
  "$HOME/.gemini/antigravity/skills/$NAME" \
  "$HOME/.agents/skills/$NAME" \
  "$HOME/.config/agents/skills/$NAME"; do
  if [ -f "$candidate/SKILL.md" ]; then
    SOURCE="$candidate"
    break
  fi
done

if [ -z "$SOURCE" ]; then
  if [ -f "$TARGET/SKILL.md" ]; then
    echo "Antigravity skill already available at $TARGET"
    exit 0
  fi
  echo "Skills CLI completed, but the Antigravity source skill was not found." >&2
  echo "Inspect: npx skills list --global" >&2
  exit 1
fi

mkdir -p "$TARGET"
# Follow symlinks produced by Skills CLI, retaining the full skill directory.
rsync -aL "$SOURCE/" "$TARGET/"
if [ ! -f "$TARGET/SKILL.md" ]; then
  echo "Antigravity installation verification failed: $TARGET/SKILL.md missing" >&2
  exit 1
fi
echo "VERIFIED Antigravity global skill: $TARGET/SKILL.md"
echo "Restart Antigravity and check Customizations > Skills."
