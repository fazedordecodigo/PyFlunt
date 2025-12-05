# Comandos úteis (PowerShell)
## Setup
- Criar/usar venv com uv: `uv venv` (opcional) e `uv pip install -e .[dev]` ou `uv sync --group dev` (se lock existir).

## Testes e qualidade
- Rodar testes + coverage: `uv run pytest --cov=flunt --cov-report=xml --cov-config=tox.ini --cov-branch`
- Checagem de tipos: `uv run mypy flunt tests`
- Lint/format automático (via pre-commit): `uv run pre-commit run --all-files --show-diff-on-failure`
- Alternativas diretas (se preferir): `uv run ruff check .` e `uv run ruff format .`

## Tox (matriz)
- `uv run tox` (ambientes py311, py312, py313, pre-commit)
- Ambiente específico: `uv run tox -e py311`

## Samples/execução
- Rodar script exemplo: `uv run sample` (usa entrypoint `samples.flunt_sample:main`)
- Ou direto: `uv run python samples/main.py`

## Docs
- Servir documentação: `uv run mkdocs serve`
- Build estático: `uv run mkdocs build`

## Util git (Windows/pwsh)
- Status: `git status`
- Diff: `git diff`
- Branches: `git branch -a`
