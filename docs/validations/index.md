# Visão Geral das Validações

O PyFlunt oferece um conjunto rico e fluente de métodos de validação prontos para uso através da classe `Contract`.

---

## Como Funcionam as Validações

Todas as validações seguem a mesma assinatura básica:

```python
.nome_da_validacao(value, ..., field, message)
```

**Parâmetros:**

- `value`: O valor a ser validado
- `...`: Parâmetros específicos da validação (ex: comprimento mínimo, valor de comparação)
- `field`: O nome do campo que está sendo validado (útil para identificar a origem do erro)
- `message`: A mensagem de erro a ser adicionada caso a validação falhe (opcional, há mensagens padrão)

**Exemplo:**

```python
from flunt.validations.contract import Contract

contract = (
    Contract()
    .requires(nome, "nome", "Nome é obrigatório")
    .is_email(email, "email", "Email inválido")
    .is_between(idade, 18, 120, "idade", "Idade deve estar entre 18 e 120")
)

if contract.is_valid:
    print("✅ Dados válidos!")
else:
    for notification in contract.get_notifications():
        print(f"❌ [{notification.field}] {notification.message}")
```

---

## Categorias de Validação

Para facilitar a consulta, as validações estão organizadas nas seguintes categorias:

### 📝 [Strings e Gerais](string.md)

Validações para strings e comparações gerais.

**Métodos disponíveis:**
- `requires()` - Verifica se um valor não está vazio
- `is_not_none_or_white_space()` - Verifica se string não é None ou whitespace
- `contains()` - Verifica se string contém outra string
- `not_contains()` - Verifica se string não contém outra string
- `is_none()` - Verifica se valor é None
- `is_not_none()` - Verifica se valor não é None
- `are_equals()` - Verifica se dois valores são iguais
- `are_not_equals()` - Verifica se dois valores são diferentes

[Ver documentação completa →](string.md)

---

### 🔢 [Numéricas](numeric.md)

Validações de tamanho de coleções (strings, listas, etc).

!!! note "Importante"
    Atualmente, estas validações operam sobre o **tamanho** (length) de coleções, não sobre valores numéricos diretos.

**Métodos disponíveis:**
- `is_greater_than()` - Tamanho maior que
- `is_greater_or_equals_than()` - Tamanho maior ou igual a
- `is_lower_than()` - Tamanho menor que
- `is_lower_or_equals_than()` - Tamanho menor ou igual a
- `is_between()` - Tamanho entre dois valores

**Exemplo:**
```python
contract.is_between(senha, 8, 128, "senha", "Senha deve ter entre 8 e 128 caracteres")
```

[Ver documentação completa →](numeric.md)

---

### 📧 [Formatos](format.md)

Validações para formatos específicos.

**Métodos disponíveis:**
- `is_email()` - Valida formato de email
- `is_not_email()` - Verifica se não é um email
- `is_credit_card()` - Valida número de cartão de crédito (algoritmo de Luhn)

**Exemplo:**
```python
contract.is_email("usuario@exemplo.com", "email", "Email inválido")
contract.is_credit_card("4532015112830366", "cartao", "Cartão inválido")
```

[Ver documentação completa →](format.md)

---

### ✓ [Booleanas](boolean.md)

Validações para valores booleanos.

**Métodos disponíveis:**
- `is_true()` - Verifica se valor é verdadeiro
- `is_false()` - Verifica se valor é falso

**Conversões automáticas:**
- `bool`: `True`, `False`
- `int`: `1` (true), `0` (false)
- `str`: `"true"`, `"yes"`, `"on"`, `"1"` (true)

**Exemplo:**
```python
contract.is_true(aceita_termos, "termos", "Você deve aceitar os termos")
contract.is_false(bloqueado, "bloqueado", "Usuário não pode estar bloqueado")
```

[Ver documentação completa →](boolean.md)

---

### 🇧🇷 [Documentos Brasileiros](brazilian_docs.md)

Validações específicas para documentos brasileiros.

!!! success "Validação Completa"
    Agora a validação de CPF e CNPJ verifica **formato** e **dígitos verificadores** (validação completa).

**Validação completa disponível:**
- Use os métodos `is_cpf()` e `is_cnpj()` para validar CPF e CNPJ com verificação dos dígitos verificadores.

**Exemplo de validação completa:**
```python
from flunt.localization.brazilian_document_validation_contract import BrazilianDocumentValidationContract

contract = BrazilianDocumentValidationContract()
contract.is_cpf("123.456.789-09", "cpf", "CPF inválido")
contract.is_cnpj("12.345.678/0001-95", "cnpj", "CNPJ inválido")
```python
from flunt.localization.flunt_regex_patterns import get_pattern
import re

cpf_pattern = get_pattern("cpf")
if re.match(cpf_pattern, "123.456.789-10"):
    print("Formato válido")
```

[Ver documentação completa →](brazilian_docs.md)

---

## Exemplo Completo

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class CadastroUsuario(Notifiable):
    def __init__(self, nome, email, senha, idade, aceita_termos):
        super().__init__()
        self.nome = nome
        self.email = email
        self.senha = senha
        self.idade = idade
        self.aceita_termos = aceita_termos

        # Validações fluentes
        contract = (
            Contract()
            # Strings
            .requires(self.nome, "nome", "Nome é obrigatório")
            .is_not_none_or_white_space(self.nome, "nome", "Nome não pode ser vazio")

            # Numéricas (tamanho)
            .is_between(self.nome, 3, 100, "nome",
                       "Nome deve ter entre 3 e 100 caracteres")
            .is_between(self.senha, 8, 128, "senha",
                       "Senha deve ter entre 8 e 128 caracteres")

            # Formatos
            .is_email(self.email, "email", "Email inválido")

            # Booleanas
            .is_true(self.aceita_termos, "termos",
                    "Você deve aceitar os termos de uso")

            # Comparações
            .is_greater_or_equals_than_number(self.idade, 18, "idade",
                                       "Você deve ter pelo menos 18 anos")
        )

        self.add_notifications(contract.get_notifications())

# Uso válido
usuario = CadastroUsuario(
    nome="João Silva",
    email="joao@exemplo.com",
    senha="SenhaSegura123!",
    idade=25,
    aceita_termos=True
)

if usuario.is_valid:
    print("✅ Cadastro válido!")

# Uso inválido
usuario_invalido = CadastroUsuario(
    nome="Jo",  # Muito curto
    email="email-invalido",  # Email inválido
    senha="123",  # Senha muito curta
    idade=16,  # Menor de idade
    aceita_termos=False  # Não aceitou termos
)

if not usuario_invalido.is_valid:
    print("❌ Erros encontrados:")
    for notification in usuario_invalido.get_notifications():
        print(f"  - [{notification.field}] {notification.message}")
```

**Saída:**
```
❌ Erros encontrados:
  - [nome] Nome deve ter entre 3 e 100 caracteres
  - [email] Email inválido
  - [senha] Senha deve ter entre 8 e 128 caracteres
  - [idade] Você deve ter pelo menos 18 anos
  - [termos] Você deve aceitar os termos de uso
```

---

## Method Chaining (Fluent API)

Uma das principais vantagens do PyFlunt é a API fluente, que permite encadear validações:

```python
contract = (
    Contract()
    .requires(nome, "nome", "Nome obrigatório")
    .is_greater_than(nome, 3, "nome", "Nome muito curto")
    .is_lower_than(nome, 100, "nome", "Nome muito longo")
    .is_email(email, "email", "Email inválido")
    .is_true(ativo, "ativo", "Deve estar ativo")
    .is_between(idade, 18, 120, "idade", "Idade inválida")
)
```

**Benefícios:**
- ✅ Código mais legível
- ✅ Validações organizadas
- ✅ Fácil manutenção
- ✅ Menos linhas de código

---

## Mensagens Padrão

Todas as validações têm mensagens padrão em inglês. Você pode:

### 1. Usar a mensagem padrão (omitindo o parâmetro)

```python
contract.is_email(email, "email")
# Usa: "The field email is not a valid email"
```

### 2. Personalizar a mensagem

```python
contract.is_email(email, "email", "Por favor, insira um email válido")
# Usa: "Por favor, insira um email válido"
```

### 3. Ver mensagens padrão disponíveis

```python
from flunt.constants.messages import (
    REQUIRED,
    IS_EMAIL,
    IS_NOT_EMAIL,
    IS_TRUE,
    IS_FALSE,
    GREATER_THAN,
    LOWER_THAN,
    IS_BETWEEN,
    # ... e outras
)

print(REQUIRED)  # "The field {0} is required"
print(IS_EMAIL)  # "The field {0} is not a valid email"
```

---

## Validações Condicionais

Você pode aplicar validações condicionalmente:

```python
contract = Contract()

# Sempre valida
contract.requires(nome, "nome", "Nome obrigatório")

# Valida apenas se premium for True
if usuario.premium:
    contract.is_true(usuario.ativo, "ativo", "Usuários premium devem estar ativos")

# Ou usando operador ternário
contract = (
    contract.is_credit_card(cartao, "cartao", "Cartão inválido")
    if requer_pagamento
    else contract
)
```

---

## Reutilizando Contracts

Você pode criar contracts reutilizáveis:

```python
class ValidadorEmail:
    @staticmethod
    def validar(email: str) -> Contract:
        return (
            Contract()
            .requires(email, "email", "Email é obrigatório")
            .is_email(email, "email", "Email inválido")
            .is_lower_than(email, 255, "email", "Email muito longo")
        )

class Usuario(Notifiable):
    def __init__(self, email):
        super().__init__()
        self.email = email

        # Reutiliza validação
        contract_email = ValidadorEmail.validar(self.email)
        self.add_notifications(contract_email.get_notifications())
```

---

## Próximos Passos

- 📖 Leia sobre o [Domain Notification Pattern](../about.md)
- 🚀 Veja o [Guia de Início Rápido](../getting-started.md)
- 💡 Consulte exemplos em [samples/](https://github.com/fazedordecodigo/PyFlunt/tree/main/samples)
- 🐛 [Reporte bugs ou sugira melhorias](https://github.com/fazedordecodigo/PyFlunt/issues)

---

## Validações Planejadas

As seguintes validações estão planejadas para versões futuras:

- ⏳ **Regex**: Validação com regex customizado
- ⏳ **Objetos**: Validações de objetos complexos

Acompanhe o desenvolvimento no [GitHub](https://github.com/fazedordecodigo/PyFlunt/issues).
