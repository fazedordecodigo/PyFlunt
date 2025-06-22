# Validações de Strings e Gerais

Estas validações são usadas para verificar o conteúdo, comprimento e outras propriedades de strings, além de realizar comparações genéricas.

---

## is_not_none_or_white_space(*value, field, message=IS_NOT_NONE_OR_WHITESPACE*)
Garante que uma string não seja `None` ou vazia.

```python
contract.is_not_none_or_white_space(nome, "Nome", "O nome não deve ser nulo ou com espaço em branco")
```

**Parameters**:

- *value ([str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/reference/datamodel.html#none))* - Valor a ser verificado.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Por padrão é retornada uma mensagem em Inglês. Caso deseje personalizar basta passar a mensagem desejada.
  - *IS_NOT_NONE_OR_WHITESPACE* = "The field {0} must not be None or Whitespace"
-----

## contains(*value*, *comparer*, *field*, *message=CONTAINS*)

Checa se a string `value` contém a substring `comparer`.

```python
contract.contains(frase, "Pyflunt", "Frase", "A frase deve conter a palavra 'Pyflunt'")
```

**Parameters**

- *value ([str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/reference/datamodel.html#none))* - String que a ser pesquisada em busca de um resultado.
- *compare ([str](https://docs.python.org/3/library/stdtypes.html#str))* - String que se deseja encontrar
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Por padrão é retornada uma mensagem em Inglês. Caso deseje personalizar basta passar a mensagem desejada.
  - CONTAINS = "The field {0} must contain {1}"
-----

## not_contains(*value, comparer, field, message=NOT_CONTAINS*)

Checa se a string `value` não contém a substring `comparer`.

```python
contract.not_contains(frase, "Pyflunt", "Frase", "A frase não deve conter a palavra 'Pyflunt'")
```

**Parameters**

- *value ([str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/reference/datamodel.html#none))* - String que a ser pesquisada em busca de um resultado.
- *compare ([str](https://docs.python.org/3/library/stdtypes.html#str))* - String que se deseja não encontrar
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Por padrão é retornada uma mensagem em Inglês. Caso deseje personalizar basta passar a mensagem desejada.
  - NOT_CONTAINS = "The field {0} must not be contain {1}"
-----
