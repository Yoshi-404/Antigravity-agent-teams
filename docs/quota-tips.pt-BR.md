# Economia de cota (plano Pro)

O plano Pro do Antigravity tem limites apertados para modelos avançados, e os relatos de usuários variam bastante. Esta estrutura foi pensada para gastar pouco.

## Regras práticas
1. **Um agente por vez.** O padrão dos workflows é sequencial. Paralelo só quando houver cota sobrando.
2. **Modelo por papel.** O campo `suggested_model` nos AGENT.md é só uma sugestão: escolha o modelo na interface do Antigravity. Use o modelo rápido (Flash) em especialistas de tarefa bem definida e o avançado (Pro) no orquestrador e nos supervisores, que tomam as decisões difíceis.
3. **Contexto enxuto.** Agentes leem só o briefing, o artefato e o handoff. Não cole histórico de conversa.
4. **Comece pequeno.** Rode o workflow com 3 ou 4 papéis antes de ligar o elenco completo. Apague de `.agents/subagents/` os papéis que não precisa.
5. **Checkpoint humano.** Os workflows pausam antes da etapa mais cara (implementação) para você aprovar. Isso evita gastar cota em direção errada.
6. **Limite de rejeições.** São 2 por artefato. Isso evita loops infinitos de retrabalho que queimam cota.

## Se a cota acabar no meio do ciclo
Tudo fica em `work/<ciclo>/`, com `status.md` mostrando a etapa atual. Retome depois dizendo ao orquestrador: "continue o ciclo <id> a partir do status.md".
