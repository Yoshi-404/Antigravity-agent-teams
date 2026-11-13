# Como personalizar

## Remover ou adicionar papéis
1. Crie `.agents/subagents/<nome>/AGENT.md` copiando um existente.
2. Defina `role`, `reviewed_by` e `skills`.
3. No supervisor responsável, adicione o nome em `reviews`.
4. Cite o papel no workflow desejado com `@nome`.
5. Rode `python ../../shared/validate.py .` (a partir desta pasta) para checar referências.

Para remover um papel, faça o caminho inverso e ajuste os workflows.

## Começar só com validação
Use apenas `ceo`, `product-manager`, `growth-marketer`, `analista-financeiro`, `analista-juridico` e os supervisores `cpo`, `cgo` e `cfo`, e rode somente `/validar-ideia`. Remova engenharia até decidir seguir.

## Trocar de idioma
Os arquivos estão em português do Brasil. Peça ao Gemini para traduzir os AGENT.md e SKILL.md mantendo o frontmatter intacto.
