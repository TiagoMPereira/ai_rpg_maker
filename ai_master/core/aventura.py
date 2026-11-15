"""
core/aventura.py — Ciclo de vida da pasta de uma aventura.

- Cria a pasta NNN-nome/ em data/aventuras/ a partir dos arquivos enviados.
- Valida os JSONs (fichas e estado) contra o sistema.json da aventura.
- Gera o estado.json e o diario.jsonl iniciais.
- Carrega todos os artefatos da aventura para a memória.
- Apaga a pasta ao deletar a aventura.
- Mantém o catálogo do core/db.py sincronizado.
"""
