# Universal Prompt Optimizer

A cross-provider Agent Skill that analyzes prompts, recommends suitable OpenAI, Gemini, or Claude models and supported reasoning configurations, then produces copy-ready optimized prompts.

This repository replaces the former Claude-only `claude-reprompt` with **`universal-prompt-optimizer`**. The older `claude-reprompt` skill remains in the repository only as an optional compatibility alias.

## Install globally with npx (recommended)

Requires Node.js 22.20 or later and access to GitHub. Run this on **your own computer** to make the skill available across your projects in Codex, Claude Code, Gemini CLI, and Antigravity:

```sh
npx skills add mirkomilmukhtorov/claude-reprompt --skill universal-prompt-optimizer --global --agent codex --agent claude-code --agent gemini-cli --agent antigravity --yes
```

This installs the **new skill only**; it does not install the legacy alias. Agent flags use the identifiers documented by the [Vercel Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/agents.md). The CLI determines each agent's installation path.

If you want to install the new skill for every agent supported by your Skills CLI rather than the four above, use:

```sh
npx skills add mirkomilmukhtorov/claude-reprompt --skill universal-prompt-optimizer --global --agent '*' --yes
```

### Replace an old Claude Reprompt installation

After verifying the new skill is available, you can remove the old global installation if you no longer need the `/claude-reprompt` command:

```sh
npx skills remove claude-reprompt --global --agent claude-code --yes
```

This removal is **optional**; the new installation does not overwrite or delete the old one.

### Check your installation

```sh
npx skills list --global
```

Look for `universal-prompt-optimizer` and the intended agents. Restart the agents if they do not refresh skill discovery automatically. For Gemini CLI, `/skills reload` also refreshes discovery.

## Use

Ask your agent:

```text
/universal-prompt-optimizer Rewrite this prompt for the best available model, recommend a supported reasoning configuration, and preserve all constraints: [your prompt]
```

Or run the offline baseline router from within the skill folder:

```sh
python3 scripts/optimizer.py --prompt 'Audit my repository read-only'
```

The Python router uses static model metadata; an AI agent is still required for semantic rewriting and live model-availability verification.

## Development and verification

```sh
python3 scripts/validate_registry.py
python3 scripts/validate_skill.py
```

The repository also includes research notes, provider-specific references, templates, and model registry metadata. The registry snapshot is dated November 7, 2026: reverify model availability, model/API IDs, reasoning settings, and pricing with official sources before consequential use.

An installation command executed in a remote container does **not** install the skill on your Mac. Run the npx command in a Terminal session on the machine whose agents should load the skill.
