# AGENTS.md

## Visão rápida do projeto
- Biblioteca Python que implementa o Domain Notification Pattern (inspirada no Flunt .NET). Núcleo em `flunt/` com `Notifiable` e contratos de validação fluent.
- Requer Python >= 3.11, zero dependências de runtime. Dev tooling via `uv`, `ruff`, `mypy`, `pytest`, `pre-commit`, `mkdocs`.
- Estrutura chave: `flunt/notifications/` (Notifiable/Notification), `flunt/validations/` (contratos), `flunt/localization/` (regex), `flunt/constants/` (mensagens), `tests/` (pytest), `docs/` (mkdocs), `samples/` (entrypoint `sample`).

## Workflows e comandos essenciais (PowerShell)
- Instalar deps dev: `uv sync --group dev` (ou `uv pip install -e .[dev]`).
- Testes rápidos: `uv run pytest --maxfail=1`. Testes + cobertura: `uv run pytest --cov=flunt --cov-report=xml --cov-config=tox.ini --cov-branch`.
- Tipos: `uv run mypy flunt tests`.
- Lint/format: `uv run pre-commit run --all-files --show-diff-on-failure` (ou `uv run ruff format .` e `uv run ruff check .`).
- Docs preview: `uv run mkdocs serve`. Sample CLI: `uv run sample` (chama `samples.flunt_sample:main`).

## Padrões de código e estilo
- Ruff: `line-length=79`, `target-version=py311`, `docstring-code-format=true`, `preview=true`. Diversas regras ativas; ignora D100/D103/D104/D203/D206/D212/D417/E501/G004/TD004/TD003/W191/PLE1205; testes ignoram S101/S603.
- Mypy estrito: `disallow_untyped_defs`, `check_untyped_defs`, `no_implicit_optional`, `disallow_any_unimported` etc. Sempre tipar funções/métodos.
- Preferir APIs de contrato/Notifiable em vez de exceções para regras de domínio.

## Contratos e validações (versão 3.1.0)
- Base: `flunt.validations.contract.Contract` (requerimentos, strings, coleções, e agora helpers para URL, data/hora, números).
- Contratos especializados: `NumericValidationContract` (faixas/limites/sinal), `DateTimeValidationContract` (intervalos min/max), `UrlValidationContract`, `BrazilianDocumentValidationContract` (CPF/CNPJ), além dos existentes de strings, coleções, e-mail, cartão, boolean.
- Testes de referência: `tests/validations/test_numeric_validation_contract.py`, `test_brazilian_document_validation_contract.py`, demais em `tests/validations/`.

## Infra/CI e automação
- Pipelines de CI incluem Python 3.14 nos testes.
- Prompts e guias em `.github/prompts/` e instruções adicionais para Copilot.

## Organização e pontos de atenção
- Código público exportado via `flunt/__init__.py`; mantenha compatibilidade de API.
- Mensagens/regex em `flunt/localization/flunt_regex_patterns.py` e `flunt/constants/messages.py`.
- Novos métodos de validação devem adicionar notificações via `add_notification`/`add_notifications` e seguir padrão de mensagens formatadas.
- Documentação vive em `docs/validations/` e `docs/about.md`; sincronize README se API pública mudar.
- Versão em `pyproject.toml`; changelog em `CHANGELOG.md` (Keep a Changelog).

## Fluxo de contribuição/práticas
- Rodar testes + mypy + lint antes de PR (ver comandos acima).
- Commits: preferir Conventional Commits (`feat/fix/chore/docs...`).
- CI: workflows em `.github/workflows/*` (linters/tests/publish), com permissões explícitas.

## Exemplos úteis
- Uso básico: `flunt/notifications/notifiable.py` mostra como armazenar notificações; `flunt/validations/contract.py` demonstra encadeamento de validações.
- Exemplos de cenário numérico/CPF: veja os testes citados para mensagens esperadas e padrões de uso.

## O que evitar
- Não lançar exceções para validações de domínio; use notificações/contratos.
- Não adicionar dependências de runtime sem necessidade (biblioteca é zero-deps).
- Evitar alterar largura de linha/estilo fora das regras do Ruff.
