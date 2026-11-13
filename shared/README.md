# shared/

Partes comuns a todos os times, mantidas em um lugar só.

- `skills/review-gate` e `skills/handoff`: protocolo de aprovação e de entrega.
- `work/_templates`: modelos de briefing, handoff, revisão, status e backlog.
- `validate.py`: valida um time (`python shared/validate.py teams/online-store`).
- `validate_all.py`: valida todos e confere se as cópias estão sincronizadas.
- `sync_shared.py`: copia as partes compartilhadas para cada time.

Cada time precisa funcionar sozinho quando alguém copia só a pasta dele, por isso as cópias existem dentro de `teams/*`. **Edite em `shared/` e rode `python shared/sync_shared.py`.**
