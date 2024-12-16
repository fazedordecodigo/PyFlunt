PORTUGUÊS | [ENGLISH](https://github.com/fazedordecodigo/PyFlunt/blob/main/docs/CHANGELOG_EN.md)

# Registro de Alterações

Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Mantenha um Registro de Alterações](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/spec/v2.0.0.html).

## [Não Lançado]
- Adicionar mensagens padronizadas em PT-BR e EN [#18](https://github.com/fazedordecodigo/PyFlunt/issues/18)
- Adicionar validação de DateTime [#27](https://github.com/fazedordecodigo/PyFlunt/issues/27)
- Adicionar validação de Números [#28](https://github.com/fazedordecodigo/PyFlunt/issues/28)
- Adicionar validação de documentos [#29](https://github.com/fazedordecodigo/PyFlunt/issues/29)
- Adicionar validação de Objetos [#31](https://github.com/fazedordecodigo/PyFlunt/issues/31)
- Adicionar validação de Regex [#32](https://github.com/fazedordecodigo/PyFlunt/issues/32)
- Adicionar validação de URL [#33](https://github.com/fazedordecodigo/PyFlunt/issues/33)
- Adicionar Result Pattner [#61](https://github.com/fazedordecodigo/PyFlunt/issues/61)
- Refatorar FluntRegexPatterns [#129](https://github.com/fazedordecodigo/PyFlux/issues/129)

## [2.3.1] - 2024-12-16
### Adicionado
- Refactoração para `get_pattern` em `CreditCardValidationContract` e `EmailValidationContract`.

### Corrigido
- Garantindo que os padrões regex retornem dados válidos para validações.
- Refatorar FluntRegexPatterns [#129](https://github.com/fazedordecodigo/PyFlux/issues/129)

## [2.3.0] - 2024-03-17
### Adicionado
- Validação de Collections [#30](https://github.com/fazedordecodigo/PyFlunt/issues/30)

### Corrigido
- Falta de tipagem de retorno nos overloads de Requires [#59](https://github.com/fazedordecodigo/PyFlunt/issues/59)
- Pipeline Linters com path quebrado para o requirements.txt [#60](https://github.com/fazedordecodigo/PyFlunt/issues/60)

## [2.2.0] - 2024-03-13
### Adicionado
- Validação UUID aplicando Duck Typing [#11](https://github.com/fazedordecodigo/PyFlunt/issues/11)
- Novos cenários de teste unitários

### Corrigido
- Links do README quebrados [#53](https://github.com/fazedordecodigo/PyFlunt/issues/53)
- Bug em `requires` que retornava falso positivo ao receber o valor booleano `False`.
- Reescrita dos testes unitários existentes.



## [2.1.1] - 2024-02-27
### Corrigido
- Links do README quebrados [#53](https://github.com/fazedordecodigo/PyFlunt/issues/53)
- Comandos para script de execução do pre-commit [#53](https://github.com/fazedordecodigo/PyFlunt/issues/53)
- Forma de comunicação para Reportar uma Vulnerabilidade [#53](https://github.com/fazedordecodigo/PyFlunt/issues/53)

## [2.1.0] - 2024-02-24
### Adicionado
- CONTRIBUTING em PT-BR e EN [#39](https://github.com/fazedordecodigo/PyFlunt/issues/39)
- CODE_OF_CONDUCT em PT-BR e EN [#40](https://github.com/fazedordecodigo/PyFlunt/issues/40)
- README em PT-BR [#41](https://github.com/fazedordecodigo/PyFlunt/issues/41)
- CHANGELOG em PT-BR e EN [#42](https://github.com/fazedordecodigo/PyFlunt/issues/42)
- SECURITY em PT-BR e EN [#43](https://github.com/fazedordecodigo/PyFlunt/issues/43)
- FUNDING [#44](https://github.com/fazedordecodigo/PyFlunt/issues/44)
- Pull Request Template em PT-BR [#45](https://github.com/fazedordecodigo/PyFlunt/issues/45)
- Issue Template Bug Report em PT-BR [#46](https://github.com/fazedordecodigo/PyFlunt/issues/46)
- Issue Template Feature Report em PT-BR [#47](https://github.com/fazedordecodigo/PyFlunt/issues/47)
- Issue Template Vulnerability Report em PT-BR [#48](https://github.com/fazedordecodigo/PyFlunt/issues/48)

### Corrigido
- Bug que impedia rodar no python v3.9 [#36](https://github.com/fazedordecodigo/PyFlunt/issues/36)

## [2.0.0] - 2024-02-13
### Adicionado

- Add Python setup and dependencies installation by @fazedordecodigo in #25

### Modificado

- Atualizado CD by @fazedordecodigo in #16
- Atualizado issue templates by @fazedordecodigo in #20
- Atualizado actions by @fazedordecodigo in #24

## [1.0.0] - 2023-05-22
### Adicionado

- Implementada CD. Versão 0.2.0 by @fazedordecodigo in #9

## [0.2.0] - 2021-11-22
### Adicionado

- Criado LICENSE by @fazedordecodigo in #4
- Implementados novos métodos is_false, is_true, is_note_none, is_none. by @fazedordecodigo in #8

### Modificado

- Editado Readme by @fazedordecodigo in #3 and #5
- Ajustes no CI by @fazedordecodigo in #6 and #7

## [0.1.1] - 2021-11-19
### Adicionado

- Lançamento by @fazedordecodigo in #1



<br>
<br>
<br>

[2.2.0](https://github.com/fazedordecodigo/PyFlunt/compare/v2.1.1...v2.2.0)

[2.1.1](https://github.com/fazedordecodigo/PyFlunt/compare/v2.1.0...v2.1.1)

[2.1.0](https://github.com/fazedordecodigo/PyFlunt/compare/v2.0.0...v2.1.0)

[2.0.0](https://github.com/fazedordecodigo/PyFlunt/compare/v1.0.0...v2.0.0)

[1.0.0](https://github.com/fazedordecodigo/PyFlunt/compare/0.2.0...v1.0.0)

[0.2.0](https://github.com/fazedordecodigo/PyFlunt/compare/0.1.1...0.2.0)

[0.1.1](https://github.com/fazedordecodigo/PyFlunt/commits/0.1.1)
