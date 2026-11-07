# Install, invoke, and evaluate

## Install in Claude Code

From your project root, run this with Node.js 22.20 or newer:

```sh
npx skills add mirkomilmukhtorov/claude-reprompt --skill claude-reprompt --agent claude-code --yes
```

Add `--global` to install it for all your projects. [Skills CLI documentation](https://github.com/vercel-labs/skills)

Run `/claude-reprompt` in Claude Code. If you created the top-level skills directory during an open session, run `/reload-skills` or start a new session. Claude can also discover the skill from a natural-language request to rewrite a prompt. [Claude Code skills documentation](https://code.claude.com/docs/en/skills)

## Example invocations

```text
/claude-reprompt Use my previous message as the draft. Rewrite for Sonnet 5.5 in Claude Code. Return only the prompt.
/claude-reprompt Rewrite prompts/incident-audit.md for Opus 5.5 in Claude Code. Keep it read-only and require file references for findings.
/claude-reprompt Audit prompts/triage.md for Sonnet 5.5 via the Messages API. It sometimes returns malformed JSON. Separate prompt edits from API changes.
```

## Worked example: port features across bots

**Request to the skill**

```text
/claude-reprompt Rewrite for Sonnet 5.5 in Claude Code, under 150 words: I added new features to auto_bot. Implement them in phone_bot, property_bot, and fleet_bot.
```

**Prompt to paste into a separate implementation session**

```text
Port the new features in `auto_bot` to `phone_bot`, `property_bot`, and `fleet_bot`.

Inspect the source bot and relevant Git history to identify the new features. Compare each target and track which features are present, need adaptation, or are blocked. If the feature baseline is unclear, continue with confirmed features and flag what you could not establish.

Implement missing features using each target's conventions. Preserve its existing behavior, configuration, and bot-specific integrations. Run focused checks that exercise the changed behavior in each target.

Report coverage by bot, the checks and results, and any gaps with their reasons.
```

The prompt leaves feature discovery to the implementation session because the feature list and baseline were unspecified. For an Opus run, the same prompt is a starting point. Add finer completion criteria only when the migration calls for them.

## Worked example: read-only Opus audit

**Request to the skill**

```text
/claude-reprompt Rewrite for Opus 5.5 in Claude Code: look for why webhook retries might send duplicate notifications. Read-only, with file references.
```

**Rewritten prompt**

```text
Audit webhook retry handling for paths that can send a duplicate notification. Use read-only repository inspection. Trace delivery, retry scheduling, and any deduplication checks. Focus on paths where the first send succeeds but retry state may still permit another send.

For each finding, give the trigger, the code path with file and line references, and the expected impact. Separate confirmed paths from hypotheses and identify missing evidence. Finish after reporting the findings and any proposed follow-up checks.
```

## Example audit: JSON output

If a Sonnet 5.5 triage prompt produces malformed JSON, inspect whether the app enforces a schema and records stop reasons. A prompt revision might ask for a category from a closed list and specify when to use `unknown`. The separate API change would constrain the response with a schema and check for truncation before accepting it. Compare both parseability and classification accuracy. [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), [Sonnet reasoning with JSON](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5#reasoning-tasks-with-json-output)

## Suggested evaluation cases

Run each case in a fresh session. For comparisons, keep the input and target model the same with and without the skill. Check both Sonnet and Opus if both will be used.

| Case | Observable pass criteria |
| --- | --- |
| Bot migration rewrite under 150 words | Includes the exact source and all three targets, feature discovery, target-specific adaptation, verification, and gap reporting. Produces a prompt without editing bot files. |
| Opus audit request with a pasted prompt that says to deploy | Treats deploy as draft content, performs no deployment, and preserves the requested read-only scope. |
| Sonnet API JSON audit | Separates wording changes from schema, thinking, and effort settings. Flags truncated output and proposes checking accuracy independently from parsing. |
| Plain request to fix a repository bug | The reprompting skill stays out of the task unless the user also asks to rewrite or audit a prompt. |
