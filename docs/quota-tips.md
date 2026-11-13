# Quota tips (limited plans)

Antigravity's paid entry plan has tight limits for advanced models, and user reports vary a lot. These teams are designed to spend little.

1. **One agent at a time.** Workflows are sequential by default.
2. **Model per role.** `suggested_model` in each AGENT.md is only a hint; choose the model in the UI. Use the fast model (Flash) for well-defined specialist tasks and the advanced one for the orchestrator and supervisors.
3. **Lean context.** Agents read only the brief, the artifact and the handoff. Don't paste chat history.
4. **Start small.** Run a workflow with 3 or 4 roles before enabling the whole cast. Delete unused roles from `.agents/subagents/`.
5. **Human checkpoint.** Workflows pause before the most expensive step so you can approve the direction.
6. **Rejection cap.** 2 per deliverable avoids endless rework loops that burn quota.

If quota runs out mid-cycle, everything is in `work/<cycle>/` and `status.md` shows the current step. Resume with: "continue cycle <id> from status.md".
