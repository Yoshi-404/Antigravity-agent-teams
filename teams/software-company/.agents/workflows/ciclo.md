---
description: Executa um ciclo completo: ideia, spec, design, implementação, qualidade, deploy e comunicação.
---

# /ciclo

Entrada: descrição do que o humano quer construir.

Siga as etapas em ordem. Um agente por vez. Em toda etapa com revisor, aplique `review-gate` (máx. 2 rejeições; 3ª escala ao @diretor).

1. **Briefing**: @diretor cria `work/<ciclo>/`, preenche `briefing.md` e `status.md`. Se faltar informação essencial, pergunta ao humano.
2. **Spec**: @product-manager escreve `01-spec.md`. @head-de-produto revisa.
3. **Design**: @arquiteto escreve `02-design.md`. @tech-lead revisa.
4. **CHECKPOINT HUMANO**: @diretor resume spec e design em até 15 linhas e pede OK antes de implementar. Pare aqui até receber resposta.
5. **Backend**: @dev-backend implementa e escreve handoff. @tech-lead revisa (rodando os testes).
6. **Frontend**: @dev-frontend implementa e escreve handoff. @tech-lead revisa.
7. **Qualidade**: @qa-engineer escreve plano e relatório; @security-engineer faz a revisão. @head-de-qualidade decide o gate com `release-checklist`. Se rejeitar, volte ao passo 5 ou 6 só para os itens apontados.
8. **Infra**: @devops entrega pipeline e plano de deploy. @tech-lead revisa.
9. **Documentação e comunicação**: @tech-writer e @marketing produzem seus artefatos. @head-de-produto revisa.
10. **Fechamento**: @diretor escreve `99-relatorio.md` e apresenta ao humano. Deploy em produção só com OK explícito.

Atualize `status.md` ao fim de cada etapa.
