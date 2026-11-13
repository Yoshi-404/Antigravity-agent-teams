# Como personalizar

## Remover ou adicionar disciplinas
1. Crie `.agents/subagents/<nome>/AGENT.md` copiando um existente.
2. Defina `role`, `reviewed_by` e `skills`.
3. No supervisor responsável, adicione o nome em `reviews`.
4. Cite o papel no workflow desejado com `@nome`.
5. Rode `python ../../shared/validate.py .` (a partir desta pasta).

## Time pequeno (solo dev)
Mantenha `produtor`, `game-designer`, `gameplay-programmer`, `qa-tester` e os supervisores correspondentes (`diretor-criativo`, `lead-programmer`, `qa-lead`). Remova os demais e ajuste os workflows.

## Por engine
Preencha a seção Projeto de `.agents/AGENTS.md`. Se quiser regras específicas (por exemplo, convenções de GDScript ou C# para Unity), crie uma skill `convencoes-<engine>` e adicione a `gameplay-programmer` e `lead-programmer`.

## Arte e áudio
Os agentes só especificam. Para ligar uma ferramenta de geração, adicione uma skill descrevendo como chamá-la e o formato de saída, e mantenha o registro de licença na `asset-spec`.

## Trocar de idioma
Peça ao Gemini para traduzir os AGENT.md e SKILL.md mantendo o frontmatter intacto.
