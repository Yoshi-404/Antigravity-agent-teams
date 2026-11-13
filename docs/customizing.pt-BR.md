# Como personalizar

Cada time tem um `CUSTOMIZING.md` com dicas específicas. Em geral:

## Adicionar ou remover papéis
1. Crie `.agents/subagents/<nome>/AGENT.md` copiando um existente.
2. Defina `role`, `reviewed_by` e `skills`.
3. No supervisor responsável, adicione o nome em `reviews`.
4. Cite o papel no workflow com `@nome`.
5. Rode `python shared/validate_all.py` na raiz do repositório.

## Trocar de idioma
Peça ao Gemini para traduzir os AGENT.md, SKILL.md e workflows mantendo o frontmatter (`name`, `role`, `reviewed_by`, `reviews`, `skills`) e os nomes de agentes citados com `@` intactos. Rode a validação depois.

## Mudar `review-gate` ou `handoff` em todos os times
Edite em `shared/` e rode `python shared/sync_shared.py`.
