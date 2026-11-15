"""
core/estado.py — Leitura, validação e atualização do estado.json e das fichas.

- Aplica as mudanças propostas pelo mestre: PV, inventário, condições, local,
  missões e flags.
- Recusa mudanças inválidas (ex.: condição inexistente no sistema.json).
- Salva em disco de forma segura: escreve em arquivo temporário e renomeia.
"""
