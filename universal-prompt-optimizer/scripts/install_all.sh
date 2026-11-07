#!/bin/sh
# Compatibility wrapper. Preferred install command is in the repository README.
# Uses the supported Skills CLI instead of copying files to guessed agent paths.
set -eu
if ! command -v npx >/dev/null 2>&1; then
  echo "npx is required. Install Node.js 22.20 or newer first." >&2
  exit 1
fi
exec npx skills add mirkomilmukhtorov/claude-reprompt \
  --skill universal-prompt-optimizer \
  --global \
  --agent codex \
  --agent claude-code \
  --agent gemini-cli \
  --agent antigravity \
  --yes
