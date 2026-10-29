# config.py — the ONE place model names live. Every other file imports from here.
# Model names change: check https://docs.claude.com/en/docs/about-claude/models/overview
MODEL = "claude-opus-5-5"          # main model: planning, PRD writing, specs
SMALL_MODEL = "claude-haiku-5-5"   # cheaper, faster model; only used for routing (Modules 16-17)
MAX_TOKENS = 16000                 # per-response output cap
MAX_ITERATIONS = 25                # hard stop for any agent loop
