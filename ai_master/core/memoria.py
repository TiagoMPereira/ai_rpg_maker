"""
core/memoria.py — Gestão de contexto de longo prazo.

- A cada N turnos, pede ao Claude que atualize o resumo.md com o que aconteceu.
- Decide quantas mensagens recentes do diário entram no contexto do próximo turno.
"""
