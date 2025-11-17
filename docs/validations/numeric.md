# Validações Numéricas

Estas validações são usadas para verificar valores numéricos (`int`, `float`) diretamente, como se um número é positivo, negativo, maior que outro, ou está dentro de um intervalo.

!!! note "Importante"
    Estas validações operam sobre **valores numéricos** (int, float), não sobre o tamanho de coleções. Para validar o comprimento de uma string, lista, ou qualquer objeto que implemente `__len__`, utilize as validações de coleção.

---

## is_greater_than_number(*value, comparer, field, message=GREATER_THAN*)

Verifica se um valor numérico é **maior que** um valor especificado.

```python
contract.is_greater_than_number(10, 5, "idade", "A idade deve ser maior que 5")
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

contract = NumericValidationContract()
contract.is_greater_than_number(10, 5, "idade", "A idade deve ser maior que 5")
# ✅ Válido: 10 > 5
```

-----

## is_greater_or_equals_than_number(*value, comparer, field, message=GREATER_OR_EQUALS_THAN*)

Verifica se um valor numérico é **maior ou igual a** um valor especificado.

```python
contract.is_greater_or_equals_than_number(18, 18, "idade", "A idade deve ser pelo menos 18")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *comparer ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor mínimo permitido (inclusivo).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *GREATER_OR_EQUALS_THAN* = "The field {0} must be greater than or equal to {1}"

**Exemplo**:

```python
contract = NumericValidationContract()
contract.is_greater_or_equals_than_number(18, 18, "idade", "Deve ter pelo menos 18 anos")
# ✅ Válido: 18 >= 18
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
contract = NumericValidationContract()
contract.is_lower_than_number(15, 18, "idade", "Idade deve ser menor que 18")
# ✅ Válido: 15 < 18
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
contract = NumericValidationContract()
contract.is_lower_or_equals_than_number(18, 18, "idade", "Idade deve ser no máximo 18")
# ✅ Válido: 18 <= 18
```

-----

## is_between_numbers(*value, min_value, max_value, field, message=BETWEEN*)

Verifica se um valor numérico está **entre** dois valores (inclusivo).

```python
contract.is_between_numbers(7, 5, 10, "idade", "A idade deve estar entre 5 e 10")
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
contract = NumericValidationContract()
contract.is_between_numbers(7, 5, 10, "idade", "A idade deve estar entre 5 e 10")
# ✅ Válido: 5 <= 7 <= 10
```

-----

## is_positive(*value, field, message=POSITIVE*)

Verifica se um valor numérico é **positivo**.

```python
contract.is_positive(7, "saldo", "O saldo deve ser positivo")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *POSITIVE* = "The field {0} must be positive"

**Exemplo**:

```python
contract = NumericValidationContract()
contract.is_positive(7, "saldo", "O saldo deve ser positivo")
# ✅ Válido: 7 > 0
```

-----

## is_negative(*value, field, message=NEGATIVE*)

Verifica se um valor numérico é **negativo**.

```python
contract.is_negative(-3, "temperatura", "A temperatura deve ser negativa")
```

**Parâmetros**:

- *value ([int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float))* - Valor a ser verificado.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *NEGATIVE* = "The field {0} must be negative"

**Exemplo**:

```python
contract = NumericValidationContract()
contract.is_negative(-3, "temperatura", "A temperatura deve ser negativa")
# ✅ Válido: -3 < 0
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
contract = NumericValidationContract()
contract.is_zero(0, "contador", "O contador deve ser zero")
# ✅ Válido: 0 == 0
```

-----

## is_not_zero(*value, field, message=NOT_ZERO*)

Verifica se um valor numérico **não é zero**.

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
contract = NumericValidationContract()
contract.is_not_zero(5, "divisor", "O divisor não pode ser zero")
# ✅ Válido: 5 != 0
```

-----

## Exemplo Completo

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.numeric_validation_contract import NumericValidationContract

class Produto(Notifiable):
    def __init__(self, preco, desconto, quantidade, estoque_minimo, estoque_maximo):
        super().__init__()
        self.preco = preco
        self.desconto = desconto
        self.quantidade = quantidade
        self.estoque_minimo = estoque_minimo
        self.estoque_maximo = estoque_maximo

        # Criando contrato de validação
        contract = (
            NumericValidationContract()
            .is_positive(self.preco, "preco", "O preço deve ser positivo")
            .is_between_numbers(self.desconto, 0, 100, "desconto",
                               "Desconto deve estar entre 0 e 100")
            .is_greater_than_number(self.quantidade, 0, "quantidade",
                                   "Quantidade deve ser maior que 0")
            .is_greater_or_equals_than_number(self.estoque_minimo, 0, "estoque_minimo",
                                             "Estoque mínimo deve ser pelo menos 0")
            .is_greater_than_number(self.estoque_maximo, self.estoque_minimo, "estoque_maximo",
                                   "Estoque máximo deve ser maior que o mínimo")
        )

        self.add_notifications(contract.get_notifications())

# Uso
produto = Produto(
    preco=99.90,
    desconto=10,
    quantidade=50,
    estoque_minimo=10,
    estoque_maximo=100
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

Estas validações funcionam com tipos numéricos:

- **Inteiros**: `int`
- **Ponto flutuante**: `float`

!!! warning "Atenção"
    Se o valor for `None`, a validação falhará e uma notificação será adicionada. Certifique-se de que os valores numéricos não são `None` antes de validá-los.
