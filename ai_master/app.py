"""
app.py — Ponto de entrada do Streamlit.

Executar com: streamlit run app.py

Responsabilidades:
- Configurar a página do Streamlit (título, layout, ícone).
- Carregar as variáveis de ambiente do .env (ANTHROPIC_API_KEY, modelo padrão).
- Garantir que o banco data/rpg.db e a pasta data/aventuras/ existam.
- Mostrar a tela inicial com a aventura ativa (se houver) e atalhos para as páginas
  Aventuras, Mesa e História.
"""
