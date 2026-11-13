---
description: Revisão independente de um código ou documento existente, sem implementar nada.
---

# /revisar

Entrada: caminho do que será revisado e o que importa (segurança, qualidade, clareza).

1. @diretor define o escopo e quais revisores entram.
2. @tech-lead revisa código e arquitetura.
3. @security-engineer revisa segurança, se pedido.
4. @head-de-qualidade consolida o que foi achado em uma lista priorizada.
5. @diretor entrega ao humano: achados por severidade e os 3 próximos passos recomendados.

Ninguém altera o código neste fluxo. A saída é um relatório em `work/<ciclo>/99-relatorio.md`.
