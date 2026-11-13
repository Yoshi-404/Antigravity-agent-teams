---
description: Executa um ciclo de desenvolvimento de uma funcionalidade: design, implementação, arte/áudio, teste e revisão.
---

# /sprint

Entrada: a funcionalidade ou mecânica a entregar.

Um agente por vez. Aplique `review-gate` (máx. 2 rejeições; 3ª escala ao @produtor).

1. **Briefing**: @produtor cria `work/<ciclo>/` e delimita o escopo.
2. **Design**: @game-designer escreve o GDD da mecânica (`write-gdd`). @diretor-criativo revisa.
3. **Conteúdo** (se a funcionalidade precisar): @level-designer e/ou @narrative-designer. @diretor-criativo revisa.
4. **Especificação de arte e áudio** (se precisar): @diretor-de-arte e @audio-designer. @diretor-criativo revisa.
5. **CHECKPOINT HUMANO**: @produtor resume o que será implementado e confirma antes de gastar cota em código.
6. **Código**: @gameplay-programmer implementa. @lead-programmer revisa rodando o projeto ou os testes.
7. **Integração**: @technical-artist e/ou @engine-programmer integram assets e ajustam desempenho. @lead-programmer revisa.
8. **Teste**: @qa-tester testa e escreve o relatório. @qa-lead decide o gate com `build-checklist`. Se rejeitar, volta ao passo 6 só para os itens apontados.
9. **Fechamento**: @produtor escreve `99-relatorio.md` com o que ficou jogável, o que foi cortado e os riscos.
