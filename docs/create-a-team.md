# Creating a new team / Criando um novo time

1. Copy the closest folder in `teams/` to `teams/<new-team>/` (or start from `.agents/` with `AGENTS.md`, `subagents/`, `skills/`, `workflows/`).
2. Keep exactly **one** orchestrator (`role: orquestrador`), **supervisors** (`role: supervisor`, with `reviews: [...]`) and **specialists** (`role: especialista`, with `reviewed_by`). Every specialist needs a supervisor who lists them.
3. Keep `review-gate` and `handoff` (run `python shared/sync_shared.py`).
4. Write workflows with human checkpoints and `@agent` mentions.
5. In `.agents/AGENTS.md`, state what the agents do **not** do (publish, spend, deploy...) and add the fill-in block.
6. Rule of thumb: every number or fact is either sourced or labeled "hypothesis" / `A CONFIRMAR`.
7. Run `python shared/validate_all.py` and add the team to the root README table.

Pt: copie o time mais parecido, mantenha 1 orquestrador, supervisores que listam seus especialistas em `reviews`, rode `sync_shared.py` e `validate_all.py`, e adicione ao README da raiz.
