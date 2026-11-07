# Claude Reprompt

A Claude Code skill that turns rough instructions into ready-to-paste prompts for Claude Sonnet and Opus. It also audits existing prompts and helps adapt them when you switch models.

## Install

From your project root, run this with Node.js 22.20 or newer:

```sh
npx skills add mirkomilmukhtorov/claude-reprompt --skill claude-reprompt --agent claude-code --yes
```

Add `--global` to install it for all your projects.

Open Claude Code and try:

```text
/claude-reprompt Rewrite for Sonnet 5.5: Port the new features in auto_bot to phone_bot, property_bot, and fleet_bot. Keep the prompt under 150 words.
```

The [worked example](claude-reprompt/references/examples.md#worked-example-port-features-across-bots) shows how the rewrite turns that request into feature discovery, target-specific implementation, and verification steps. The command returns a prompt for a separate implementation session.

## What it covers

- [Prompting rules and sources](claude-reprompt/references/prompting.md) for clarity, examples, tool use, structured output, and evaluation.
- [Sonnet and Opus guidance](claude-reprompt/references/models.md) for model selection, effort, thinking modes, and migration. Claude Code controls and Messages API settings are covered separately.
- [Examples and evaluation cases](claude-reprompt/references/examples.md) for a feature migration, a read-only audit, and a JSON failure.

The skill uses your active Claude Code session's model and effort. If it helps, star the repo so you can find it again.
