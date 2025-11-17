# Validações Booleanas

Estas validações são usadas para verificar valores booleanos, com suporte para conversão automática de diferentes tipos.

---

## is_true(*value, field, message=IS_TRUE*)

Verifica se um valor é verdadeiro (`True`).

```python
contract.is_true(usuario_ativo, "ativo", "Usuário deve estar ativo")
```

**Parâmetros**:

- *value ([bool](https://docs.python.org/3/library/stdtypes.html#bool) | [int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str))* - Valor a ser verificado.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *IS_TRUE* = "The field {0} must be True"

**Conversão Automática**:

A validação aceita diferentes tipos e os converte automaticamente:

| Tipo | Valor | Resultado |
|------|-------|-----------|
| `bool` | `True` | ✅ Verdadeiro |
| `bool` | `False` | ❌ Falso |
| `int` | `1` (ou qualquer != 0) | ✅ Verdadeiro |
| `int` | `0` | ❌ Falso |
| `str` | `"true"`, `"True"`, `"TRUE"` | ✅ Verdadeiro |
| `str` | `"1"` | ✅ Verdadeiro |
| `str` | `"yes"`, `"Yes"`, `"YES"` | ✅ Verdadeiro |
| `str` | `"on"`, `"On"`, `"ON"` | ✅ Verdadeiro |
| `str` | `"false"`, `"0"`, `"no"`, etc | ❌ Falso |

**Exemplo de uso**:

```python
from flunt.validations.contract import Contract

contract = Contract()

# Valores booleanos diretos
contract.is_true(True, "ativo")
print(contract.is_valid)  # True

contract.is_true(False, "ativo", "Deve estar ativo")
print(contract.is_valid)  # False

# Valores inteiros
contract = Contract()
contract.is_true(1, "habilitado")
print(contract.is_valid)  # True

contract.is_true(0, "habilitado")
print(contract.is_valid)  # False

# Valores string (case-insensitive)
contract = Contract()
contract.is_true("true", "confirmado")
print(contract.is_valid)  # True

contract.is_true("TRUE", "confirmado")
print(contract.is_valid)  # True

contract.is_true("yes", "aceito")
print(contract.is_valid)  # True

contract.is_true("on", "ligado")
print(contract.is_valid)  # True

contract.is_true("false", "confirmado")
print(contract.is_valid)  # False
```

-----

## is_false(*value, field, message=IS_FALSE*)

Verifica se um valor é falso (`False`).

```python
contract.is_false(usuario_bloqueado, "bloqueado", "Usuário não pode estar bloqueado")
```

**Parâmetros**:

- *value ([bool](https://docs.python.org/3/library/stdtypes.html#bool) | [int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str))* - Valor a ser verificado.
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo a ser verificado.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *IS_FALSE* = "The field {0} must be False"

**Conversão Automática**:

Segue as mesmas regras de conversão do `is_true`, mas com lógica invertida:

| Tipo | Valor | Resultado |
|------|-------|-----------|
| `bool` | `False` | ✅ Falso (válido) |
| `bool` | `True` | ❌ Verdadeiro (inválido) |
| `int` | `0` | ✅ Falso (válido) |
| `int` | `1` (ou qualquer != 0) | ❌ Verdadeiro (inválido) |
| `str` | `"false"`, `"0"`, etc | ✅ Falso (válido) |
| `str` | `"true"`, `"1"`, `"yes"`, `"on"` | ❌ Verdadeiro (inválido) |

**Exemplo de uso**:

```python
from flunt.validations.contract import Contract

contract = Contract()

# Valores booleanos
contract.is_false(False, "bloqueado")
print(contract.is_valid)  # True

contract.is_false(True, "bloqueado", "Usuário não deve estar bloqueado")
print(contract.is_valid)  # False

# Valores inteiros
contract = Contract()
contract.is_false(0, "tentativas_falhas")
print(contract.is_valid)  # True

contract.is_false(3, "tentativas_falhas")
print(contract.is_valid)  # False

# Valores string
contract = Contract()
contract.is_false("false", "notificacoes")
print(contract.is_valid)  # True

contract.is_false("0", "notificacoes")
print(contract.is_valid)  # True

contract.is_false("true", "notificacoes")
print(contract.is_valid)  # False
```

-----

## Casos de Uso Práticos

### 1. Validar Termos de Uso

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class CadastroUsuario(Notifiable):
    def __init__(self, nome, email, aceita_termos, aceita_marketing):
        super().__init__()
        self.nome = nome
        self.email = email
        self.aceita_termos = aceita_termos
        self.aceita_marketing = aceita_marketing

        contract = (
            Contract()
            # Termos de uso são obrigatórios
            .is_true(self.aceita_termos, "aceita_termos",
                    "Você deve aceitar os termos de uso")

            # Marketing deve estar desabilitado por padrão (LGPD/GDPR)
            .is_false(self.aceita_marketing, "aceita_marketing",
                     "Marketing deve ser opt-in explícito")
        )

        self.add_notifications(contract.get_notifications())

# Cadastro válido
usuario = CadastroUsuario(
    nome="João Silva",
    email="joao@exemplo.com",
    aceita_termos=True,  # ✅ Aceitou os termos
    aceita_marketing=False  # ✅ Marketing desabilitado
)

print(usuario.is_valid)  # True

# Cadastro inválido
usuario_invalido = CadastroUsuario(
    nome="Maria Santos",
    email="maria@exemplo.com",
    aceita_termos=False,  # ❌ Não aceitou os termos
    aceita_marketing=True  # ❌ Marketing habilitado por padrão
)

if not usuario_invalido.is_valid:
    for notification in usuario_invalido.get_notifications():
        print(f"❌ {notification.message}")
```

### 2. Validar Estado de Entidade

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class Pedido(Notifiable):
    def __init__(self, numero, pago, cancelado, enviado):
        super().__init__()
        self.numero = numero
        self.pago = pago
        self.cancelado = cancelado
        self.enviado = enviado

        contract = Contract()

        # Para enviar, o pedido deve estar pago
        if enviado:
            contract.is_true(self.pago, "pago",
                           "Pedido deve estar pago antes de ser enviado")

        # Pedido não pode estar cancelado se for enviado
        if enviado:
            contract.is_false(self.cancelado, "cancelado",
                            "Pedido cancelado não pode ser enviado")

        self.add_notifications(contract.get_notifications())

# Cenário válido
pedido = Pedido(
    numero="PED-123",
    pago=True,
    cancelado=False,
    enviado=True
)

print(pedido.is_valid)  # True

# Cenário inválido
pedido_invalido = Pedido(
    numero="PED-456",
    pago=False,  # ❌ Não pago
    cancelado=True,  # ❌ Cancelado
    enviado=True  # Tentando enviar
)

print(pedido_invalido.is_valid)  # False
```

### 3. Validar Flags de Feature (Feature Toggles)

```python
from flunt.validations.contract import Contract

class ConfiguracaoAplicacao:
    def __init__(self, modo_debug, modo_producao, cache_habilitado):
        self.modo_debug = modo_debug
        self.modo_producao = modo_producao
        self.cache_habilitado = cache_habilitado

    def validar(self):
        contract = Contract()

        # Em produção, debug deve estar desabilitado
        if self.modo_producao:
            contract.is_false(self.modo_debug, "modo_debug",
                            "Debug deve estar desabilitado em produção")

        # Em produção, cache deve estar habilitado
        if self.modo_producao:
            contract.is_true(self.cache_habilitado, "cache_habilitado",
                           "Cache deve estar habilitado em produção")

        return contract

# Configuração válida para produção
config_prod = ConfiguracaoAplicacao(
    modo_debug=False,  # ✅ Debug desabilitado
    modo_producao=True,
    cache_habilitado=True  # ✅ Cache habilitado
)

contract = config_prod.validar()
print(contract.is_valid)  # True

# Configuração inválida para produção
config_invalida = ConfiguracaoAplicacao(
    modo_debug=True,  # ❌ Debug habilitado em produção!
    modo_producao=True,
    cache_habilitado=False  # ❌ Cache desabilitado
)

contract = config_invalida.validar()
if not contract.is_valid:
    for notification in contract.get_notifications():
        print(f"⚠️ {notification.message}")
```

### 4. Validar Formulário Web (com strings)

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class FormularioContato(Notifiable):
    """Processar dados de formulário web (strings)."""

    def __init__(self, nome, email, newsletter, termos):
        super().__init__()
        self.nome = nome
        self.email = email
        self.newsletter = newsletter  # "true" ou "false" do form
        self.termos = termos  # "on" ou None do checkbox

        contract = (
            Contract()
            # Nome e email obrigatórios
            .requires(self.nome, "nome", "Nome é obrigatório")
            .is_email(self.email, "email", "E-mail inválido")

            # Termos devem ser aceitos (checkbox "on")
            .is_true(self.termos or "", "termos",
                    "Você deve aceitar os termos")
        )

        self.add_notifications(contract.get_notifications())

# Simulando dados do formulário
form_data = {
    "nome": "João Silva",
    "email": "joao@exemplo.com",
    "newsletter": "true",  # String do form
    "termos": "on"  # Checkbox marcado
}

formulario = FormularioContato(**form_data)

if formulario.is_valid:
    print("✅ Formulário válido!")
    print(f"Newsletter: {formulario.newsletter}")  # "true"
```

-----

## Valores Aceitos como Verdadeiros

As seguintes strings são consideradas **verdadeiras** (case-insensitive):

- `"true"`
- `"1"`
- `"yes"`
- `"on"`

Qualquer outro valor de string é considerado **falso**, incluindo:

- `"false"`
- `"0"`
- `"no"`
- `"off"`
- Strings vazias `""`
- Qualquer outra string

-----

## Combinando com Outras Validações

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class Usuario(Notifiable):
    def __init__(self, email, idade, premium, ativo):
        super().__init__()
        self.email = email
        self.idade = idade
        self.premium = premium
        self.ativo = ativo

        contract = (
            Contract()
            # Email válido
            .is_email(self.email, "email", "E-mail inválido")

            # Se for premium, deve estar ativo
            .is_true(self.ativo, "ativo",
                    "Usuários premium devem estar ativos")
            if self.premium else Contract()
        )

        self.add_notifications(contract.get_notifications())
```

-----

## Diferença entre `is_true` e `requires`

```python
# requires() - verifica se valor existe (não vazio/None)
contract.requires(valor, "campo", "Campo obrigatório")

# is_true() - verifica se valor é True (booleano)
contract.is_true(valor, "campo", "Campo deve ser True")
```

**Quando usar cada um:**

- **`requires()`**: Use para campos obrigatórios (nome, email, etc)
- **`is_true()`**: Use para flags booleanas que DEVEM ser verdadeiras (aceitar termos, estar ativo, etc)
- **`is_false()`**: Use para flags booleanas que DEVEM ser falsas (não bloqueado, não cancelado, etc)
