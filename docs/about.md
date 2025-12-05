# Sobre o Domain Notification Pattern

O **Domain Notification Pattern** é um padrão de design que centraliza o gerenciamento de erros e validações no nível de domínio da aplicação, evitando o uso excessivo de exceções e condicionais.

---

## O Problema

### Abordagem Tradicional com Exceções

```python
class Usuario:
    def __init__(self, nome, email, idade):
        if not nome:
            raise ValueError("Nome é obrigatório")

        if len(nome) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")

        if not email:
            raise ValueError("Email é obrigatório")

        if "@" not in email:
            raise ValueError("Email inválido")

        if idade < 18:
            raise ValueError("Usuário deve ser maior de idade")

        self.nome = nome
        self.email = email
        self.idade = idade
```

**Problemas:**

1. ❌ **Fluxo por exceção**: Exceções devem ser para situações excepcionais, não para validações de negócio
2. ❌ **Performance**: Lançar exceções tem custo computacional significativo
3. ❌ **UX ruim**: Usuário recebe apenas o primeiro erro, não todos de uma vez
4. ❌ **Código verboso**: Muitos `if/raise` poluem o código
5. ❌ **Dificulta testes**: Testar cada exceção requer blocos try/except

### Abordagem com IFs e Retornos

```python
class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.erros = []

    def validar(self):
        if not self.nome:
            self.erros.append("Nome é obrigatório")

        if self.nome and len(self.nome) < 3:
            self.erros.append("Nome deve ter pelo menos 3 caracteres")

        if not self.email:
            self.erros.append("Email é obrigatório")

        if self.email and "@" not in self.email:
            self.erros.append("Email inválido")

        if self.idade < 18:
            self.erros.append("Usuário deve ser maior de idade")

        return len(self.erros) == 0
```

**Problemas:**

1. ❌ **Alto número de IFs**: Complexidade ciclomática alta
2. ❌ **Código duplicado**: Lógica de validação espalhada
3. ❌ **Difícil manutenção**: Adicionar validações aumenta complexidade
4. ❌ **Não reutilizável**: Validações não podem ser compartilhadas

---

## A Solução: Domain Notification Pattern

### Conceito

O padrão centraliza notificações (erros, avisos, informações) em uma lista gerenciada pela própria entidade de domínio, permitindo:

1. ✅ **Coletar múltiplas validações** antes de retornar
2. ✅ **API fluente** (method chaining) para validações
3. ✅ **Separação de responsabilidades** (validação vs. lógica de negócio)
4. ✅ **Reutilização** de validações através de Contracts
5. ✅ **Sem exceções** para validações de negócio

### Implementação com PyFlunt

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class Usuario(Notifiable):
    def __init__(self, nome, email, idade):
        super().__init__()
        self.nome = nome
        self.email = email
        self.idade = idade

        # Validações em uma única chain fluente
        contract = (
            Contract()
            .requires(self.nome, "nome", "Nome é obrigatório")
            .is_greater_or_equals_than(self.nome, 3, "nome",
                                       "Nome deve ter pelo menos 3 caracteres")
            .requires(self.email, "email", "Email é obrigatório")
            .is_email(self.email, "email", "Email inválido")
            .is_greater_or_equals_than(self.idade, 18, "idade",
                                       "Usuário deve ser maior de idade")
        )

        # Adiciona todas as notificações à entidade
        self.add_notifications(contract.get_notifications())

# Uso
usuario = Usuario("Jo", "email-invalido", 16)

if usuario.is_valid:
    print("✅ Usuário válido!")
else:
    print("❌ Erros encontrados:")
    for notification in usuario.get_notifications():
        print(f"  - [{notification.field}] {notification.message}")
```

**Saída:**
```
❌ Erros encontrados:
  - [nome] Nome deve ter pelo menos 3 caracteres
  - [email] Email inválido
  - [idade] Usuário deve ser maior de idade
```

---

## Princípios do Padrão

### 1. Notifiable

Toda entidade que precisa de validação herda de `Notifiable`:

```python
class MinhaEntidade(Notifiable):
    def __init__(self):
        super().__init__()  # Inicializa lista de notificações
```

**Métodos disponíveis:**

- `add_notification(field, message)` - Adiciona uma notificação
- `add_notifications(notifications)` - Adiciona múltiplas notificações
- `get_notifications()` - Retorna lista de notificações
- `is_valid` (property) - Retorna `True` se não há notificações
- `clear()` - Limpa todas as notificações

### 2. Contract

Contracts são conjuntos reutilizáveis de validações:

```python
contract = (
    Contract()
    .requires(valor, "campo", "mensagem")
    .is_email(email, "email", "Email inválido")
    .is_between(idade, 18, 120, "idade", "Idade inválida")
)

# Obter notificações do contrato
notificacoes = contract.get_notifications()
```

### 3. Notification

Cada notificação contém:

```python
class Notification:
    field: str    # Campo que falhou
    message: str  # Mensagem de erro
```

---

## Domain-Driven Design (DDD)

O Domain Notification Pattern é especialmente útil em projetos que seguem DDD:

### Value Objects

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class Email(Notifiable):
    """Value Object para Email."""

    def __init__(self, endereco: str):
        super().__init__()
        self._endereco = endereco

        contract = (
            Contract()
            .requires(self._endereco, "email", "Email é obrigatório")
            .is_email(self._endereco, "email", "Email inválido")
        )

        self.add_notifications(contract.get_notifications())

    @property
    def endereco(self) -> str:
        return self._endereco

    def __str__(self) -> str:
        return self._endereco

# Uso
email = Email("usuario@exemplo.com")
if email.is_valid:
    print(f"Email válido: {email}")
```

### Entities

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class Produto(Notifiable):
    """Entidade Produto."""

    def __init__(self, nome: str, preco: float, estoque: int):
        super().__init__()
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

        self._validar()

    def _validar(self):
        contract = (
            Contract()
            .requires(self.nome, "nome", "Nome do produto é obrigatório")
            .is_between(self.nome, 3, 100, "nome",
                       "Nome deve ter entre 3 e 100 caracteres")
            .is_greater_than(self.preco, 0, "preco",
                            "Preço deve ser maior que zero")
            .is_greater_or_equals_than(self.estoque, 0, "estoque",
                                       "Estoque não pode ser negativo")
        )

        self.add_notifications(contract.get_notifications())

    def baixar_estoque(self, quantidade: int):
        """Baixa estoque com validação."""
        contract = Contract()

        if quantidade <= 0:
            contract.add_notification("quantidade",
                                     "Quantidade deve ser maior que zero")

        if quantidade > self.estoque:
            contract.add_notification("estoque",
                                     "Estoque insuficiente")

        self.add_notifications(contract.get_notifications())

        if contract.is_valid:
            self.estoque -= quantidade

# Uso
produto = Produto("Notebook", 2500.0, 10)

if produto.is_valid:
    produto.baixar_estoque(5)

    if produto.is_valid:
        print(f"✅ Estoque atualizado: {produto.estoque}")
    else:
        for n in produto.get_notifications():
            print(f"❌ {n.message}")
```

### Aggregates

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class Pedido(Notifiable):
    """Aggregate Root - Pedido."""

    def __init__(self, cliente_id: str):
        super().__init__()
        self.cliente_id = cliente_id
        self.itens = []
        self.finalizado = False

    def adicionar_item(self, produto_id: str, quantidade: int, preco: float):
        """Adiciona item ao pedido."""
        contract = (
            Contract()
            .requires(produto_id, "produto_id", "Produto é obrigatório")
            .is_greater_than(quantidade, 0, "quantidade",
                            "Quantidade deve ser maior que zero")
            .is_greater_than(preco, 0, "preco",
                            "Preço deve ser maior que zero")
        )

        if not contract.is_valid:
            self.add_notifications(contract.get_notifications())
            return

        item = {
            "produto_id": produto_id,
            "quantidade": quantidade,
            "preco": preco,
            "total": quantidade * preco
        }

        self.itens.append(item)

    def finalizar(self):
        """Finaliza o pedido."""
        contract = Contract()

        if len(self.itens) == 0:
            contract.add_notification("itens",
                                     "Pedido deve ter pelo menos um item")

        if self.finalizado:
            contract.add_notification("finalizado",
                                     "Pedido já foi finalizado")

        self.add_notifications(contract.get_notifications())

        if contract.is_valid:
            self.finalizado = True

    def total(self) -> float:
        """Calcula total do pedido."""
        return sum(item["total"] for item in self.itens)

# Uso
pedido = Pedido(cliente_id="CLI-123")

pedido.adicionar_item("PROD-001", 2, 100.0)
pedido.adicionar_item("PROD-002", 1, 50.0)

pedido.finalizar()

if pedido.is_valid:
    print(f"✅ Pedido finalizado! Total: R$ {pedido.total():.2f}")
else:
    for n in pedido.get_notifications():
        print(f"❌ {n.message}")
```

---

## Vantagens do Padrão

### 1. Melhor UX

```python
# ❌ Com exceções: apenas 1 erro por vez
try:
    usuario = Usuario("", "", 16)
except ValueError as e:
    print(e)  # "Nome é obrigatório" (não vê os outros erros)

# ✅ Com Notification: todos os erros de uma vez
usuario = Usuario("", "", 16)
for notification in usuario.get_notifications():
    print(notification.message)
# "Nome é obrigatório"
# "Email é obrigatório"
# "Idade deve ser maior que 18"
```

### 2. Facilita Testes

```python
def test_usuario_invalido():
    usuario = Usuario("", "email-invalido", 16)

    assert not usuario.is_valid
    assert len(usuario.get_notifications()) == 3

    # Verificar erros específicos
    erros = {n.field: n.message for n in usuario.get_notifications()}
    assert "nome" in erros
    assert "email" in erros
    assert "idade" in erros
```

### 3. API Fluente

```python
# Validações encadeadas de forma legível
contract = (
    Contract()
    .requires(nome, "nome", "Nome obrigatório")
    .is_greater_than(nome, 3, "nome", "Nome muito curto")
    .is_lower_than(nome, 100, "nome", "Nome muito longo")
    .is_email(email, "email", "Email inválido")
    .is_between(idade, 18, 120, "idade", "Idade inválida")
)
```

### 4. Integração com APIs

```python
from flask import Flask, jsonify, request
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

app = Flask(__name__)

class CriarUsuarioRequest(Notifiable):
    def __init__(self, data):
        super().__init__()
        self.nome = data.get("nome")
        self.email = data.get("email")

        contract = (
            Contract()
            .requires(self.nome, "nome", "Nome é obrigatório")
            .is_email(self.email, "email", "Email inválido")
        )

        self.add_notifications(contract.get_notifications())

@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    request_data = CriarUsuarioRequest(request.json)

    if not request_data.is_valid:
        errors = [
            {"field": n.field, "message": n.message}
            for n in request_data.get_notifications()
        ]
        return jsonify({"errors": errors}), 400

    # Criar usuário...
    return jsonify({"message": "Usuário criado com sucesso"}), 201
```

**Resposta da API:**
```json
{
  "errors": [
    {"field": "nome", "message": "Nome é obrigatório"},
    {"field": "email", "message": "Email inválido"}
  ]
}
```

---

## Quando Usar

### ✅ Use Domain Notification Pattern para:

- Validações de **regras de negócio**
- Validações de **entrada de usuário**
- **Value Objects** em DDD
- **Entities** e **Aggregates** em DDD
- **APIs REST** (retornar múltiplos erros)
- **Formulários web** (mostrar todos os erros)

### ❌ Não use para:

- **Erros técnicos** (falha de conexão, arquivo não encontrado)
- **Erros inesperados** (divisão por zero, null pointer)
- **Fluxo de controle** da aplicação
- **Situações excepcionais** (use exceções)

---

## Padrões Relacionados

### Result Pattern

Complementa o Notification Pattern retornando sucesso/falha:

```python
# Planejado para próxima versão (#61)
from flunt.results import Result

def criar_usuario(nome, email):
    usuario = Usuario(nome, email)

    if not usuario.is_valid:
        return Result.fail(usuario.get_notifications())

    # Salvar usuário...
    return Result.success(usuario)

# Uso
resultado = criar_usuario("João", "joao@email.com")

if resultado.is_success:
    print(f"✅ Sucesso: {resultado.value}")
else:
    print("❌ Erros:")
    for error in resultado.errors:
        print(f"  - {error.message}")
```

### Specification Pattern

Pode ser combinado para validações complexas:

```python
class UsuarioMaiorIdadeSpec:
    def is_satisfied_by(self, usuario):
        contract = Contract()
        contract.is_greater_or_equals_than(
            usuario.idade, 18, "idade",
            "Usuário deve ser maior de idade"
        )
        return contract.is_valid, contract.get_notifications()
```

---

## Referências e Inspirações

- **[Flunt (.NET)](https://github.com/andrebaltieri/flunt)** - Implementação original em C# por André Baltieri
- **[Martin Fowler - Notification Pattern](https://martinfowler.com/eaaDev/Notification.html)**
- **[Domain-Driven Design (Eric Evans)](https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)**
- **[Implementing Domain-Driven Design (Vaughn Vernon)](https://www.amazon.com/Implementing-Domain-Driven-Design-Vaughn-Vernon/dp/0321834577)**

---

## Outras Implementações

- **C#**: [Flunt](https://github.com/andrebaltieri/flunt) (original)
- **Java**: [JFlunt](https://github.com/carlosbritojun/jflunt)
- **JavaScript**: [Flunt.js](https://github.com/jhonesgoncal/flunt)
- **PHP**: [Flunt-PHP](https://github.com/matheusbloise/flunt-php)
- **Python**: [PyFlunt](https://github.com/fazedordecodigo/PyFlunt) (este projeto)

---

## Contribuindo

Quer ajudar a melhorar o PyFlunt? Confira:

- 📖 [Guia de Contribuição](https://github.com/fazedordecodigo/PyFlunt/blob/main/CONTRIBUTING.md)
- 🐛 [Reportar Bugs](https://github.com/fazedordecodigo/PyFlunt/issues)
- 💡 [Sugerir Funcionalidades](https://github.com/fazedordecodigo/PyFlunt/issues)
- 💬 [Discord da Comunidade](https://discord.gg/HNwFHQWX)
