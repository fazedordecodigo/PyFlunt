# Estilo e convenções
- Formatação/lint via Ruff (`line-length=79`, `indent=4`, `target-version=py311`, `fix=true`). `ruff format` usa `docstring-code-format=true`, `docstring-code-line-length=59`, `preview=true`.
- Lint `ruff check` com seleções amplas (F,E,W,D,I,N,UP,YTT,ASYNC,B,C4,DTZ,T10,LOG,G,PIE,T20,PYI,PT,Q,RSE,RET,SLF,SLOT,TID,TCH,INT,ARG,PTH,TD,PL,UP,RUF,TRY). Ignora: D100/D103/D104/D203/D206/D212/D417/E501/G004/TD004/TD003/W191/PLE1205. Testes têm ignores extras: S101,S603.
- Tipagem: mypy com `disallow_untyped_defs`, `no_implicit_optional`, `disallow_any_unimported`, `check_untyped_defs` etc. Código deve ter type hints.
- Estilo de código: Python 3.11+, foco em objetos de domínio/contratos; docstrings não obrigatórias para tudo (alguns D* ignorados). Linha máxima lógica 79.
- Preferir evitar `print` (PLE1205 ignorado, mas T20 imprime?). Uso de logging? Sem diretriz explícita. Manter notificações em vez de exceções no domínio.
- Naming: seguir PEP8; avoid wildcard imports.
