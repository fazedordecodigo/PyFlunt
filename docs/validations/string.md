# Validações de Strings e Gerais

Estas validações são usadas para verificar o conteúdo, comprimento e outras propriedades de strings, além de realizar comparações genéricas.

---

### `requires(value, field, message)`
Garante que uma string não seja nula ou vazia.

```python
contract.requires(nome, "Nome", "O nome é um campo obrigatório")
```

-----

### `is_not_null_or_empty(value, field, message)`

Verifica se uma string não é nula ou vazia.

```python
contract.is_not_null_or_empty(nome, "Nome", "O nome não pode ser vazio")
```

-----

### `is_not_null_or_whitespace(value, field, message)`

Garante que uma string não seja nula, vazia ou contenha apenas espaços em branco.

```python
contract.is_not_null_or_whitespace(nome, "Nome", "O nome não pode ser composto apenas por espaços")
```

-----

### `has_min_len(value, minimum, field, message)`

Assegura que o comprimento da string seja no mínimo o valor `minimum`.

```python
contract.has_min_len(senha, 6, "Senha", "A senha deve ter no mínimo 6 caracteres")
```

-----

### `has_max_len(value, maximum, field, message)`

Assegura que o comprimento da string seja no máximo o valor `maximum`.

```python
contract.has_max_len(resumo, 255, "Resumo", "O resumo não pode exceder 255 caracteres")
```

-----

### `has_len(value, length, field, message)`

Verifica se o comprimento da string é exatamente igual ao valor `length`.

```python
contract.has_len(uf, 2, "UF", "O campo UF deve ter exatamente 2 caracteres")
```

-----

### `contains(text, value, field, message)`

Checa se a string `text` contém a substring `value`.

```python
contract.contains(frase, "Pyflunt", "Frase", "A frase deve conter a palavra 'Pyflunt'")
```

-----

### `not_contains(text, value, field, message)`

Checa se a string `text` **não** contém a substring `value`.

```python
contract.not_contains(comentarios, "spam", "Comentários", "Comentários não podem conter a palavra 'spam'")
```

-----

### `are_equals(value, comparer, field, message)`

Compara se `value` e `comparer` são idênticos.

```python
contract.are_equals(senha, confirmacao_senha, "Confirmação de Senha", "As senhas não conferem")
```

-----

### `are_not_equals(value, comparer, field, message)`

Compara se `value` e `comparer` são diferentes.

```python
contract.are_not_equals(codigo_antigo, codigo_novo, "Código Novo", "O novo código não pode ser igual ao antigo")
```

-----

### `is_none(value, field, message)`

Verifica se um objeto é `None`.

```python
contract.is_none(item_opcional, "Item Opcional", "O item opcional deve ser nulo para esta operação")
```

-----

### `is_not_none(value, field, message)`

Verifica se um objeto **não** é `None`.

```python
contract.is_not_none(usuario_logado, "Usuário", "Um usuário deve estar logado para realizar esta ação")
```
