# Customizing

Each team has its own `CUSTOMIZING.md` (in Portuguese) with specific tips. In general:

## Add or remove roles
1. Create `.agents/subagents/<name>/AGENT.md` by copying an existing one.
2. Set `role`, `reviewed_by` and `skills`.
3. In the responsible supervisor, add the name to `reviews`.
4. Mention the role in the workflow with `@name`.
5. Run `python shared/validate_all.py` at the repo root.

## Translate
Ask Gemini to translate AGENT.md, SKILL.md and workflow files, keeping the frontmatter keys (`name`, `role`, `reviewed_by`, `reviews`, `skills`) and `@agent` mentions intact. Run validation afterwards.

## Change `review-gate` or `handoff` for every team
Edit in `shared/` and run `python shared/sync_shared.py`.
