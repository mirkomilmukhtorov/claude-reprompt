# Prompting rules and evidence

Reviewed against Anthropic documentation on 2026-11-07. Use the rules that address the user's task or a demonstrated failure.

| Situation | Rule | Official source |
| --- | --- | --- |
| Ambiguous request | Put the requested action and deliverable up front. State scope, constraints, and output requirements in concrete terms. Explain the reason for an unusual constraint when it helps Claude apply it to new cases. | [Clarity and context](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct) |
| Unstable style or categorization | Add representative examples when an instruction alone leaves room for inconsistent choices. Vary the examples, including a boundary case, and keep the expected output aligned with the rules. | [Examples](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#use-examples-effectively) |
| Mixed instructions and data | Separate requirements, examples, source material, and the task with headings or descriptive XML when the input is complex. Identify external content as data and specify how it may be used. In an integration, keep trusted instructions in the proper message role and maintain provenance. Markup by itself provides no security boundary. | [XML structure](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#structure-prompts-with-xml-tags), [Opus pasted text guidance](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#mark-pasted-text-in-user-messages) |
| Long source documents | Within the task message, place long source material before the closing question. Give each document a stable label and ask for supporting passages or source locations when grounding matters. | [Long-context prompting](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#long-context-prompting) |
| Coding or tool work | Specify the allowed action and observable end state. Name relevant evidence and ask for a check that exercises changed behavior. For plans, require a stop after the plan. For implementation, give a stopping condition tied to the requested work and its relevant checks. | [Claude Code best practices](https://code.claude.com/docs/en/best-practices), [Sonnet initiative and scope](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5#steer-initiative-and-scope) |
| Need an explanation | Ask for a short rationale, decisive evidence, assumptions, or verification results. Leave private reasoning to the model's thinking mechanism. | [Keep reasoning in thinking blocks](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#keep-reasoning-in-thinking-blocks) |
| Machine-readable output | Define fields, allowed values, and missing-data behavior. For strict API JSON, configure `output_config.format` with `type: "json_schema"` and handle incomplete or refused responses. Schema conformance and factual accuracy need separate checks. | [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) |
| Suspected prompt regression | Write down observable success criteria and compare against the original on representative inputs and edge cases. Hold model, tools, and effort fixed when comparing wording. Sweep model or effort separately if that is the suspected cause. | [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), [Build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) |

## Diagnose before adding instructions

- If the request is unclear, sharpen the deliverable, constraints, or example. Preserve project-specific rules already supplied.
- If Claude starts an unwanted action or stops early, clarify scope, allowed actions, and the condition for finishing.
- If outputs miss a schema or a tool call fails, check the schema, tool declaration, and integration error handling before adding prose.
- If the answer uses stale facts, specify the source and when to consult it. When the tool is unavailable, state how to handle unverified facts.
- If long runs look stalled, decide whether the prompt needs meaningful milestones or the application needs to render progress. Check the model-specific guide for that surface.

## Evaluate a rewrite

Choose a normal case, an edge case, and a case that should stay out of scope. Define pass criteria before running either prompt. Inspect the output or tool trace for preserved intent, permitted actions, and required evidence. For repeatable workloads, include latency and token use when they matter. Attribute any improvement to what the comparison actually tested.

The diagnostic sequence and the package's output defaults are practical choices for this skill. [Anthropic's skill authoring guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) informed the short entry point and on-demand references.
