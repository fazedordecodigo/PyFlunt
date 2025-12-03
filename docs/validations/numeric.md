# Validações Numéricas

Estas validações são usadas para verificar valores numéricos (`int`, `float`) diretamente, como se um número é positivo, negativo, maior que outro, ou está dentro de um intervalo.

!!! note "Importante"
    Estas validações operam sobre **valores numéricos** (int, float), não sobre o tamanho de coleções. Para validar o comprimento de uma string, lista, ou qualquer objeto que implemente `__len__`, utilize as validações de coleção.

---

## is_greater_than_number(*value, comparer, field, message=GREATER_THAN*)

Verifica se um valor numérico é **maior que** um valor especificado.

```python
contract.is_greater_than_number(25, 18, "idade", "A idade deve ser maior que 18")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *comparer ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor mínimo permitido (exclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *GREATER_THAN* = "The field {0} must be greater than {1}"

**Exemplo**:

```python
from flunt.validations.numeric_validation_contract import NumericValidationContract

contract = Contract()
contract.is_greater_than_number(25, 18, "idade", "A idade deve ser maior que 18")
# ✅ Válido: 25 > 18

contract.is_greater_than_number(15, 18, "idade", "A idade deve ser maior que 18")
# ❌ Inválido: 15 não é maior que 18
```

-----

## is_greater_or_equals_than_number(*value, comparer, field, message=GREATER_OR_EQUALS_THAN*)

Verifica se um valor numérico é **maior ou igual a** um valor especificado.

```python
contract.is_greater_or_equals_than_number(18, 18, "idade", "Você deve ter pelo menos 18 anos")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *comparer ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor mínimo permitido (inclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *GREATER_OR_EQUALS_THAN* = "The field {0} must be greater than or equal to {1}"

**Exemplo**:

```python
contract = Contract()
contract.is_greater_or_equals_than_number(18, 18, "idade", "Você deve ter pelo menos 18 anos")
# ✅ Válido: 18 >= 18

contract.is_greater_or_equals_than_number(17, 18, "idade", "Você deve ter pelo menos 18 anos")
# ❌ Inválido: 17 não é maior ou igual a 18
```

-----

## is_lower_than_number(*value, comparer, field, message=LOWER_THAN*)

Verifica se um valor numérico é **menor que** um valor especificado.

```python
contract.is_lower_than_number(15, 18, "idade", "A idade deve ser menor que 18")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *comparer ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor máximo permitido (exclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *LOWER_THAN* = "The field {0} must be lower than {1}"

**Exemplo**:

```python
contract = Contract()
contract.is_lower_than_number(15, 18, "idade", "A idade deve ser menor que 18")
# ✅ Válido: 15 < 18

contract.is_lower_than_number(25, 18, "idade", "A idade deve ser menor que 18")
# ❌ Inválido: 25 não é menor que 18
```

-----

## is_lower_or_equals_than_number(*value, comparer, field, message=LOWER_OR_EQUALS_THAN*)

Verifica se um valor numérico é **menor ou igual a** um valor especificado.

```python
contract.is_lower_or_equals_than_number(18, 18, "idade", "A idade deve ser no máximo 18")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *comparer ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor máximo permitido (inclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *LOWER_OR_EQUALS_THAN* = "The field {0} must be lower than or equal to {1}"

**Exemplo**:

```python
contract = Contract()
contract.is_lower_or_equals_than_number(18, 18, "idade", "A idade deve ser no máximo 18")
# ✅ Válido: 18 <= 18

contract.is_lower_or_equals_than_number(19, 18, "idade", "A idade deve ser no máximo 18")
# ❌ Inválido: 19 não é menor ou igual a 18
```

-----

## is_between_numbers(*value, min_value, max_value, field, message=BETWEEN*)

Verifica se um valor numérico está **entre** dois valores (inclusivo).

```python
contract.is_between_numbers(25, 18, 65, "idade", "A idade deve estar entre 18 e 65")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *min_value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor mínimo permitido (inclusivo).
- *max_value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor máximo permitido (inclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *BETWEEN* = "The field {0} must be between {1} and {2}"

**Exemplo**:

```python
contract = Contract()

contract.is_between_numbers(25, 18, 65, "idade", "A idade deve estar entre 18 e 65")
# ✅ Válido: 18 <= 25 <= 65

contract.is_between_numbers(70, 18, 65, "idade", "A idade deve estar entre 18 e 65")
# ❌ Inválido: 70 não está entre 18 e 65
```

-----

## is_positive(*value, field, message=POSITIVE*)

Verifica se um valor numérico é **positivo** (maior que zero).

```python
contract.is_positive(10, "saldo", "O saldo deve ser positivo")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *POSITIVE* = "The field {0} must be positive"

**Exemplo**:

```python
contract = Contract()
contract.is_positive(10, "quantidade", "A quantidade deve ser positiva")
# ✅ Válido: 10 > 0

contract.is_positive(-5, "quantidade", "A quantidade deve ser positiva")
# ❌ Inválido: -5 não é positivo

contract.is_positive(0, "quantidade", "A quantidade deve ser positiva")
# ❌ Inválido: 0 não é positivo
```

-----

## is_negative(*value, field, message=NEGATIVE*)

Verifica se um valor numérico é **negativo** (menor que zero).

```python
contract.is_negative(-10, "temperatura", "A temperatura deve ser negativa")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *NEGATIVE* = "The field {0} must be negative"

**Exemplo**:

```python
contract = Contract()
contract.is_negative(-10, "saldo", "O saldo deve ser negativo")
# ✅ Válido: -10 < 0

contract.is_negative(5, "saldo", "O saldo deve ser negativo")
# ❌ Inválido: 5 não é negativo

contract.is_negative(0, "saldo", "O saldo deve ser negativo")
# ❌ Inválido: 0 não é negativo
```

-----

## is_zero(*value, field, message=ZERO*)

Verifica se um valor numérico é **zero**.

```python
contract.is_zero(0, "contador", "O contador deve ser zero")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *ZERO* = "The field {0} must be zero"

**Exemplo**:

```python
contract = Contract()
contract.is_zero(0, "contador", "O contador deve ser zero")
# ✅ Válido: valor é 0

contract.is_zero(5, "contador", "O contador deve ser zero")
# ❌ Inválido: 5 não é zero
```

-----

## is_not_zero(*value, field, message=NOT_ZERO*)

Verifica se um valor numérico é **diferente de zero**.

```python
contract.is_not_zero(5, "divisor", "O divisor não pode ser zero")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *NOT_ZERO* = "The field {0} must not be zero"

**Exemplo**:

```python
contract = Contract()
contract.is_not_zero(5, "divisor", "O divisor não pode ser zero")
# ✅ Válido: 5 != 0

contract.is_not_zero(0, "divisor", "O divisor não pode ser zero")
# ❌ Inválido: valor é zero
```

-----

## Exemplo Completo

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.numeric_validation_contract import NumericValidationContract

class Produto(Notifiable):
    def __init__(self, preco, desconto, quantidade, temperatura_armazenamento):
        super().__init__()
        self.preco = preco
        self.desconto = desconto
        self.quantidade = quantidade
        self.temperatura_armazenamento = temperatura_armazenamento

        # Criando contrato de validação
        contract = (
            Contract()
            .is_positive(self.preco, "preco",
                        "O preço deve ser positivo")
            .is_between_numbers(self.desconto, 0, 100, "desconto",
                               "O desconto deve estar entre 0 e 100")
            .is_greater_than_number(self.quantidade, 0, "quantidade",
                                   "A quantidade deve ser maior que zero")
            .is_negative(self.temperatura_armazenamento, "temperatura",
                        "A temperatura de armazenamento deve ser negativa (congelado)")
        )

        self.add_notifications(contract.get_notifications())

# Uso
produto = Produto(
    preco=29.99,
    desconto=15,
    quantidade=50,
    temperatura_armazenamento=-18
)

if produto.is_valid:
    print("✅ Produto válido!")
else:
    print("❌ Erros de validação:")
    for notification in produto.get_notifications():
        print(f"  - {notification.message}")
```

-----

## Tipos Suportados

Estas validações funcionam com os tipos numéricos do Python:

- **Inteiros**: `int`
- **Ponto flutuante**: `float`

!!! warning "Atenção"
    Se o valor for `None`, a validação falhará e uma notificação será adicionada. Para validar que um campo numérico não é `None`, use as validações de obrigatoriedade antes das validações numéricas.
