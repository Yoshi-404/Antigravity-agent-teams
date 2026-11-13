# Como personalizar

## Remover ou adicionar papéis
1. Crie `.agents/subagents/<nome>/AGENT.md` copiando um existente.
2. Defina `role`, `reviewed_by` e `skills`.
3. No supervisor responsável, adicione o nome em `reviews`.
4. Cite o papel no workflow desejado com `@nome`.
5. Rode `python ../../shared/validate.py .` (a partir desta pasta) para checar referências.

Para remover um papel, faça o caminho inverso e ajuste os workflows.

## Começar pequeno
Mantenha `gerente-da-loja`, `especialista-de-catalogo`, `redator-de-produtos`, `analista-de-precos` e os supervisores `head-de-catalogo` e `head-comercial`; rode só `/lancar-produto`.

## Plataformas
Preencha a plataforma em `.agents/AGENTS.md`. Se quiser, crie uma skill com o formato de importação (CSV) da sua plataforma e adicione ao `especialista-de-catalogo`.

## Trocar de idioma
Os arquivos estão em português do Brasil. Peça ao Gemini para traduzir os AGENT.md e SKILL.md mantendo o frontmatter intacto.
