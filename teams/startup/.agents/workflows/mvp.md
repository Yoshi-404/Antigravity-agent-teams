---
description: Constrói o MVP: spec, UX, arquitetura, código, testes e deploy, com checkpoint antes de implementar.
---

# /mvp

Entrada: hipótese validada e escopo.

1. @ceo abre o ciclo.
2. @product-manager escreve a spec do MVP. @cpo revisa.
3. @ux-designer escreve os fluxos e telas. @cpo revisa.
4. @arquiteto escreve o design técnico com custo estimado. @cto revisa.
5. **CHECKPOINT HUMANO**: @ceo resume spec, UX e design (até 15 linhas) e pede OK antes de gastar cota com código.
6. @dev-fullstack implementa em partes pequenas. @cto revisa cada parte rodando os testes.
7. @qa-engineer testa e revisa a segurança. @cto revisa o relatório.
8. @devops entrega CI/CD, rollback e alertas de custo. @cto revisa.
9. @cto aplica `release-checklist` e emite o gate.
10. @ceo escreve `99-relatorio.md`. Deploy em produção só com OK do fundador.
