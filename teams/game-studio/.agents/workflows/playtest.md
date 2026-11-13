---
description: Roda uma sessão de teste e transforma os achados em correções e ajustes de design priorizados.
---

# /playtest

Entrada: a build ou o trecho a testar, e o que se quer descobrir.

1. @produtor define as perguntas de teste (ex.: "o jogador entende o objetivo?").
2. @qa-tester executa e escreve o relatório com `playtest-report`. Se não conseguir executar o jogo, deve dizer isso e fazer revisão estática do projeto e dos GDDs.
3. @qa-lead revisa o relatório e classifica a severidade.
4. @game-designer lê só as observações de experiência e propõe ajustes (números, regras, ensino), marcados como hipóteses. @diretor-criativo revisa.
5. @gameplay-programmer corrige os defeitos bloqueantes e altos. @lead-programmer revisa.
6. @produtor prioriza o que entra no próximo `/sprint` e registra no backlog.
