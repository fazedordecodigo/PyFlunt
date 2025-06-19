# Visão Geral das Validações

O Pyflunt oferece um conjunto rico e fluente de métodos de validação prontos para uso através da classe `Contract`.

Todas as validações seguem a mesma assinatura básica:

```python
.nome_da_validacao(value, ..., field, message)
```

  - `value`: O valor a ser validado.
  - `...`: Parâmetros específicos da validação (ex: comprimento mínimo, valor de comparação).
  - `field`: O nome do campo que está sendo validado (útil para identificar a origem do erro).
  - `message`: A mensagem de erro a ser adicionada caso a validação falhe.

## Categorias de Validação

Para facilitar a consulta, as validações estão organizadas nas seguintes categorias:

  * [**Strings e Gerais**](string.md): Validações para strings (comprimento, conteúdo) e comparações gerais.
  * [**Numéricas**](https://www.google.com/search?q=numeric.md): Validações para números, como comparações e intervalos.
  * [**Formatos**](format.md): Validações para formatos específicos, como E-mail, URL e Cartão de Crédito.
  * [**Booleanas**](https://www.google.com/search?q=boolean.md): Validações para valores `True` ou `False`.
  * [**Documentos Brasileiros**](https://www.google.com/search?q=brazilian_docs.md): Validações específicas para documentos como CPF e CNPJ.
