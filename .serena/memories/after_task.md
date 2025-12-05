# Checklist pós-tarefa
1) Garantir formatação/lint:
   - `uv run pre-commit run --all-files --show-diff-on-failure`
   - Opcional/rápido: `uv run ruff format .` e `uv run ruff check .`
2) Garantir tipos: `uv run mypy flunt tests`
3) Garantir testes: `uv run pytest --cov=flunt --cov-report=xml --cov-config=tox.ini --cov-branch`
4) Verificar cobertura/relatórios conforme necessário (`coverage.xml`).
5) Atualizar changelog/docs se mudança de comportamento público.
6) `git status` para conferir alterações; `git diff` para revisão final.
