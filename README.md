# Harness Engineering

A single-page course on **harness engineering**: everything around an LLM that turns it into a working agent. That means the loop, tools, context, skills, hooks, sub-agents, guardrails, evals, and cost and latency controls.

All 18 modules use one running example, a **PM Agent** that turns Notion meeting notes into a PRD, writes OpenSpec specs, waits for human approval, then creates a Trello card and a GitHub pull request.

## Open the course

Open `harness-engineering.html` in any browser. It's one self-contained file. Diagrams and syntax highlighting load from cdnjs, so the first view needs an internet connection.

## Run the capstone agent

`pm_agent.py` is a complete minimal harness. Notion, Trello and GitHub are mocked, so the only account it needs is a Claude API key.

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install anthropic
export ANTHROPIC_API_KEY="..."      # never commit this
python pm_agent.py mtg-101 mtg-102  # answer 'y' at the review prompt
```

- `config.py` is the only place the model name lives. Check [docs.claude.com](https://docs.claude.com/en/docs/about-claude/models/overview) for current model names.
- Output goes to `pm_agent_out/`, including an audit log of every tool call in `pm_agent_out/tools.jsonl`.
- Optional: set `PRICE_IN_PER_MTOK` and `PRICE_OUT_PER_MTOK` (from the official pricing page) to see the run's cost in dollars.

## Notes

Details that change often, such as OpenSpec commands, hook event names, SDK options and integration endpoints, are marked **"Verify in docs"** in the course, with links to the official docs.
