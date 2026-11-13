---
description: Fluxo curto para corrigir um defeito: reproduzir, corrigir, testar e revisar.
---

# /hotfix

Entrada: descrição do defeito.

1. @diretor abre `work/<ciclo>/` e registra o defeito.
2. @qa-engineer reproduz e escreve passos exatos e o teste que falha.
3. @dev-backend ou @dev-frontend (o dono da área) corrige com o menor diff possível e confirma que o teste passa. Handoff curto.
4. @tech-lead revisa o diff e roda os testes.
5. @security-engineer entra só se o defeito toca autenticação, autorização, entrada de usuário ou dados sensíveis.
6. @head-de-qualidade confirma que não há regressão e emite o gate.
7. @diretor relata ao humano. Deploy só com OK explícito.

Limite: 2 rejeições por etapa; depois escalar.
