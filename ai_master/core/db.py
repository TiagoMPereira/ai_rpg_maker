"""
core/db.py — Acesso ao SQLite (data/rpg.db).

- Cria a tabela `aventuras` se não existir.
- Expõe as operações do catálogo: registrar, listar, buscar, atualizar
  status/turno/data e remover.
- Guarda apenas metadados; o conteúdo da aventura fica nos arquivos da pasta dela.

Esquema:

    CREATE TABLE aventuras (
      id            INTEGER PRIMARY KEY,
      nome          TEXT NOT NULL,
      pasta         TEXT UNIQUE NOT NULL,
      status        TEXT DEFAULT 'em_andamento', -- em_andamento | arquivada | concluida
      turno         INTEGER DEFAULT 0,
      criada_em     TEXT,
      atualizada_em TEXT
    );
"""
