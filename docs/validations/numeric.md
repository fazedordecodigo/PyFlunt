# Validações Numéricas

Estas validações são usadas para verificar o tamanho de coleções (strings, listas, dicionários, tuplas, etc.) através de comparações numéricas.

!!! note "Importante"
    Atualmente, estas validações operam sobre o **tamanho** (length) de coleções, não sobre valores numéricos diretos. Para validar o comprimento de uma string, lista, ou qualquer objeto que implemente `__len__`, use os métodos abaixo.

---

## is_lower_than(*value, comparer, field, message=LOWER_THAN*)

Verifica se o tamanho de uma coleção é **menor que** um valor especificado.

```python
contract.is_lower_than(nome, 50, "nome", "O nome deve ter menos de 50 caracteres")
```

**Parâmetros**:

- *value ([Sized](https://docs.python.org/3/library/typing.html#typing.Sized))* - Coleção a ser verificada (str, list, dict, set, tuple, etc.).
- *comparer ([int](https://docs.python.org/3/library/functions.html#int))* - Valor máximo permitido (exclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *LOWER_THAN* = "The field {0} must have less than {1} items"

**Exemplo**:

```python
from flunt.validations.contract import Contract

# Validar tamanho de string
contract = Contract()
contract.is_lower_than("João", 10, "nome", "Nome muito longo")
# ✅ Válido: len("João") = 4 < 10

# Validar tamanho de lista
items = [1, 2, 3]
contract.is_lower_than(items, 5, "items", "Muitos itens")
# ✅ Válido: len(items) = 3 < 5
```

-----

## is_lower_or_equals_than(*value, comparer, field, message=LOWER_OR_EQUALS_THAN*)

Verifica se o tamanho de uma coleção é **menor ou igual a** um valor especificado.

```python
contract.is_lower_or_equals_than(senha, 20, "senha", "A senha deve ter no máximo 20 caracteres")
```

**Parâmetros**:

- *value ([Sized](https://docs.python.org/3/library/typing.html#typing.Sized))* - Coleção a ser verificada.
- *comparer ([int](https://docs.python.org/3/library/functions.html#int))* - Valor máximo permitido (inclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *LOWER_OR_EQUALS_THAN* = "The field {0} must have {1} items or less"

**Exemplo**:

```python
contract = Contract()
contract.is_lower_or_equals_than("12345", 5, "codigo", "Código deve ter no máximo 5 dígitos")
# ✅ Válido: len("12345") = 5 <= 5
```

-----

## is_greater_than(*value, comparer, field, message=GREATER_THAN*)

Verifica se o tamanho de uma coleção é **maior que** um valor especificado.

```python
contract.is_greater_than(descricao, 10, "descricao", "A descrição deve ter mais de 10 caracteres")
```

**Parâmetros**:

- *value ([Sized](https://docs.python.org/3/library/typing.html#typing.Sized))* - Coleção a ser verificada.
- *comparer ([int](https://docs.python.org/3/library/functions.html#int))* - Valor mínimo permitido (exclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *GREATER_THAN* = "The field {0} must have more than {1} items"

**Exemplo**:

```python
contract = Contract()
contract.is_greater_than("Descrição detalhada do produto", 5, "descricao")
# ✅ Válido: len(descricao) = 33 > 5

# Validar que uma lista não está vazia
tags = ["python", "ddd", "validation"]
contract.is_greater_than(tags, 0, "tags", "Deve haver pelo menos uma tag")
# ✅ Válido: len(tags) = 3 > 0
```

-----

## is_greater_or_equals_than(*value, comparer, field, message=GREATER_OR_EQUALS_THAN*)

Verifica se o tamanho de uma coleção é **maior ou igual a** um valor especificado.

```python
contract.is_greater_or_equals_than(nome, 3, "nome", "O nome deve ter pelo menos 3 caracteres")
```

**Parâmetros**:

- *value ([Sized](https://docs.python.org/3/library/typing.html#typing.Sized))* - Coleção a ser verificada.
- *comparer ([int](https://docs.python.org/3/library/functions.html#int))* - Valor mínimo permitido (inclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *GREATER_OR_EQUALS_THAN* = "The field {0} must have {1} items or more"

**Exemplo**:

```python
contract = Contract()
contract.is_greater_or_equals_than("Ana", 3, "nome", "Nome deve ter no mínimo 3 caracteres")
# ✅ Válido: len("Ana") = 3 >= 3
```

-----

## is_between(*value, min, max, field, message=IS_BETWEEN*)

Verifica se o tamanho de uma coleção está **entre** dois valores (inclusivo).

```python
contract.is_between(username, 3, 20, "username", "Username deve ter entre 3 e 20 caracteres")
```

**Parâmetros**:

- *value ([Sized](https://docs.python.org/3/library/typing.html#typing.Sized))* - Coleção a ser verificada.
- *min ([int](https://docs.python.org/3/library/functions.html#int))* - Valor mínimo permitido (inclusivo).
- *max ([int](https://docs.python.org/3/library/functions.html#int))* - Valor máximo permitido (inclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *IS_BETWEEN* = "The field {0} must have between {1} and {2} items"

**Exemplo**:

```python
contract = Contract()

# Validar tamanho de senha
contract.is_between("senha123", 8, 32, "senha", "Senha deve ter entre 8 e 32 caracteres")
# ✅ Válido: 8 <= len("senha123") = 8 <= 32

# Validar quantidade de itens em uma lista
opcoes = ["A", "B", "C"]
contract.is_between(opcoes, 2, 5, "opcoes", "Deve haver entre 2 e 5 opções")
# ✅ Válido: 2 <= len(opcoes) = 3 <= 5
```

-----

## Exemplo Completo

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class Usuario(Notifiable):
    def __init__(self, username, senha, bio, tags):
        super().__init__()
        self.username = username
        self.senha = senha
        self.bio = bio
        self.tags = tags

        # Criando contrato de validação
        contract = (
            Contract()
            .is_between(self.username, 3, 20, "username",
                       "Username deve ter entre 3 e 20 caracteres")
            .is_between(self.senha, 8, 128, "senha",
                       "Senha deve ter entre 8 e 128 caracteres")
            .is_lower_or_equals_than(self.bio, 500, "bio",
                                     "Bio deve ter no máximo 500 caracteres")
            .is_greater_than(self.tags, 0, "tags",
                            "Deve haver pelo menos uma tag")
            .is_lower_or_equals_than(self.tags, 10, "tags",
                                     "Máximo de 10 tags permitidas")
        )

        self.add_notifications(contract.get_notifications())

# Uso
usuario = Usuario(
    username="joaosilva",
    senha="SenhaSegura123!",
    bio="Desenvolvedor Python apaixonado por DDD",
    tags=["python", "ddd", "clean-code"]
)

if usuario.is_valid:
    print("✅ Usuário válido!")
else:
    print("❌ Erros de validação:")
    for notification in usuario.get_notifications():
        print(f"  - {notification.message}")
```

-----

## Tipos Suportados

Estas validações funcionam com qualquer tipo que implemente `__len__` (protocolo `Sized`):

- **Strings**: `str`
- **Listas**: `list`
- **Tuplas**: `tuple`
- **Conjuntos**: `set`, `frozenset`
- **Dicionários**: `dict`
- **Bytes**: `bytes`, `bytearray`
- **Ranges**: `range`

!!! warning "Atenção"
    Se o valor não for iterável (não tiver `__len__`), uma notificação será adicionada com a mensagem `IS_NOT_SIZED`.
