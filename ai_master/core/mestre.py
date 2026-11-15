"""
core/mestre.py — Integração com o Claude.

- Monta o contexto de cada turno: prompt base (prompts/mestre.md), regras
  (sistema.md/sistema.json), mundo, fichas, estado, resumo e últimas mensagens do diário.
- Faz a chamada à API em streaming.
- Interpreta a resposta estruturada do mestre: narração, tipo de pedido (escolha ou
  rolagem), opções e mudanças de estado propostas.
"""
