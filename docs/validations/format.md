# Validações de Formato

Estas validações são usadas para verificar se valores seguem formatos específicos, como emails e cartões de crédito.

---

## is_email(*value, field, message=IS_EMAIL*)

Valida se uma string é um endereço de e-mail válido usando expressão regular.

```python
contract.is_email(email, "email", "E-mail inválido")
```

**Parâmetros**:

- *value ([str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/reference/datamodel.html#none))* - String a ser validada como e-mail.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *IS_EMAIL* = "The field {0} is not a valid email"

**Padrão de validação**:
```regex
^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$
```

**Exemplos válidos**:
- `usuario@exemplo.com`
- `nome.sobrenome@empresa.com.br`
- `user+tag@dominio.co`
- `admin123@test-server.org`

**Exemplos inválidos**:
- `email_sem_arroba.com`
- `@dominio.com` (falta usuário)
- `usuario@` (falta domínio)
- `usuario@dominio` (falta TLD)

**Exemplo de uso**:

```python
from flunt.validations.contract import Contract

contract = Contract()

# E-mail válido
contract.is_email("joao@exemplo.com", "email")
print(contract.is_valid)  # True

# E-mail inválido
contract.is_email("email-invalido", "email", "Formato de e-mail incorreto")
print(contract.is_valid)  # False
print(contract.notifications[0].message)  # "Formato de e-mail incorreto"

# None ou string vazia são inválidos
contract.is_email(None, "email")
print(contract.is_valid)  # False
```

-----

## is_not_email(*value, field, message=IS_NOT_EMAIL*)

Valida se uma string **não** é um endereço de e-mail válido.

```python
contract.is_not_email(username, "username", "Username não pode ser um e-mail")
```

**Parâmetros**:

- *value ([str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/reference/datamodel.html#none))* - String a ser validada.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *IS_NOT_EMAIL* = "The field {0} must not be an email"

**Exemplo de uso**:

```python
from flunt.validations.contract import Contract

contract = Contract()

# Username não é e-mail (válido)
contract.is_not_email("joaosilva123", "username")
print(contract.is_valid)  # True

# Username é e-mail (inválido)
contract.is_not_email("joao@email.com", "username",
                      "Use um username, não um e-mail")
print(contract.is_valid)  # False
```

-----

## is_credit_card(*value, field, message=IS_NOT_CREDIT_CARD*)

Valida se uma string é um número de cartão de crédito válido usando o **Algoritmo de Luhn**.

```python
contract.is_credit_card(numero_cartao, "cartao", "Cartão de crédito inválido")
```

**Parâmetros**:

- *value ([str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/reference/datamodel.html#none))* - String contendo apenas números do cartão.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *IS_NOT_CREDIT_CARD* = "The field {0} must not be a valid Credit Card"

**Algoritmo de Luhn**:

O [Algoritmo de Luhn](https://pt.wikipedia.org/wiki/Algoritmo_de_Luhn) é um método de checksum usado para validar números de identificação, incluindo cartões de crédito. Ele detecta erros de digitação simples.

**Bandeiras suportadas** (via algoritmo):
- Visa (16 dígitos)
- Mastercard (16 dígitos)
- American Express (15 dígitos)
- Discover (16 dígitos)
- Diners Club (14 dígitos)
- E outras que sigam o padrão Luhn

**Importante**:
- O número deve conter **apenas dígitos** (sem espaços, traços ou pontos)
- A validação verifica o checksum, não a existência real do cartão
- Não valida data de validade ou CVV

**Exemplos válidos** (números de teste):
```python
# Visa
"4532015112830366"
"4556737586899855"

# Mastercard
"5425233430109903"
"2221000000000009"

# American Express
"374245455400126"
"378282246310005"
```

**Exemplos inválidos**:
```python
"4532015112830367"  # Checksum inválido (último dígito errado)
"1234567890123456"  # Não passa no algoritmo de Luhn
"4532-0151-1283-0366"  # Contém caracteres não numéricos
"abcd1234"  # Contém letras
None  # Valor nulo
```

**Exemplo de uso**:

```python
from flunt.validations.contract import Contract

contract = Contract()

# Cartão válido (teste Visa)
contract.is_credit_card("4532015112830366", "cartao")
print(contract.is_valid)  # True

# Cartão inválido
contract.is_credit_card("1234567890123456", "cartao",
                        "Número de cartão inválido")
print(contract.is_valid)  # False

# Cartão com formatação (inválido)
contract.is_credit_card("4532-0151-1283-0366", "cartao")
print(contract.is_valid)  # False (deve conter apenas números)
```

**Removendo formatação antes de validar**:

```python
from flunt.validations.contract import Contract

def validar_cartao(numero_formatado):
    # Remove espaços, traços e pontos
    numero_limpo = numero_formatado.replace(" ", "").replace("-", "").replace(".", "")

    contract = Contract()
    contract.is_credit_card(numero_limpo, "cartao", "Cartão inválido")

    return contract.is_valid

# Agora funciona com formatação
print(validar_cartao("4532 0151 1283 0366"))  # True
print(validar_cartao("4532-0151-1283-0366"))  # True
```

-----

## Exemplo Completo - Cadastro de Usuário

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class CadastroUsuario(Notifiable):
    def __init__(self, email, username, cartao):
        super().__init__()
        self.email = email
        self.username = username
        self.cartao = cartao

        # Limpar formatação do cartão
        cartao_limpo = self.cartao.replace(" ", "").replace("-", "")

        # Validações
        contract = (
            Contract()
            # Email deve ser válido
            .is_email(self.email, "email", "E-mail inválido")

            # Username não pode ser um e-mail
            .is_not_email(self.username, "username",
                         "Use um username, não um e-mail")

            # Username deve ter tamanho adequado
            .is_between(self.username, 3, 20, "username",
                       "Username deve ter entre 3 e 20 caracteres")

            # Cartão deve ser válido (se fornecido)
            .is_credit_card(cartao_limpo, "cartao",
                           "Cartão de crédito inválido")
        )

        self.add_notifications(contract.get_notifications())

# Exemplo de uso válido
cadastro = CadastroUsuario(
    email="joao@exemplo.com",
    username="joaosilva",
    cartao="4532 0151 1283 0366"
)

if cadastro.is_valid:
    print("✅ Cadastro válido!")
else:
    print("❌ Erros de validação:")
    for notification in cadastro.get_notifications():
        print(f"  - [{notification.field}] {notification.message}")

# Exemplo de uso inválido
cadastro_invalido = CadastroUsuario(
    email="email-invalido",  # ❌ Email inválido
    username="user@email.com",  # ❌ Username não pode ser email
    cartao="1234-5678-9012-3456"  # ❌ Cartão inválido
)

if not cadastro_invalido.is_valid:
    print("\n❌ Cadastro inválido:")
    for notification in cadastro_invalido.get_notifications():
        print(f"  - [{notification.field}] {notification.message}")
```

**Saída esperada**:
```
✅ Cadastro válido!

❌ Cadastro inválido:
  - [email] E-mail inválido
  - [username] Use um username, não um e-mail
  - [cartao] Cartão de crédito inválido
```

-----

## Próximas Validações (Planejadas)

As seguintes validações de formato estão planejadas para versões futuras:

- **URL**: Validar URLs (http/https)
- **Telefone**: Validar números de telefone
- **CEP**: Validar CEP brasileiro
- **Passport**: Validar números de passaporte
- **Regex customizado**: Permitir validação com regex personalizado

Para acompanhar o desenvolvimento, veja as [issues no GitHub](https://github.com/fazedordecodigo/PyFlunt/issues).
