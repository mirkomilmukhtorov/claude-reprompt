# Reasoning configuration selection

Simple extraction/reformatting: lowest available reasoning. Routine analysis and bounded coding: medium, when supported. Hard debugging, architecture and complex mathematics: high. Max/xhigh only after observed quality benefits justify latency and cost. Gemini uses thinking_level, OpenAI reasoning.effort, Claude output_config.effort; the names are not interchangeable. Never infer API values from consumer app labels; reject unsupported values.
