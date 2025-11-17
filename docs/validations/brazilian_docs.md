# Validações de Documentos Brasileiros

PyFlunt oferece suporte completo para validação de documentos brasileiros, com foco em CPF e CNPJ.

!!! success "Validação Completa Implementada"
    O PyFlunt agora valida **formato E dígitos verificadores** de CPF e CNPJ! A implementação completa garante que apenas documentos brasileiros válidos sejam aceitos.

---

## Validação Completa de CPF e CNPJ

### is_cpf(*value, field, message=IS_NOT_CPF*)

Valida se uma string é um CPF válido com verificação completa de dígitos verificadores.

```python
from flunt.validations.contract import Contract

contract = Contract().is_cpf("123.456.789-09", "cpf", "CPF inválido")
```

**Parâmetros**:

- *value ([str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/reference/datamodel.html#none))* - CPF a ser validado (com ou sem formatação).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *IS_NOT_CPF* = "The field {0} must not be a valid CPF"

**Validações realizadas**:
1. ✅ Formato correto (11 dígitos)
2. ✅ Rejeita números sequenciais (111.111.111-11, 000.000.000-00, etc.)
3. ✅ Valida primeiro dígito verificador
4. ✅ Valida segundo dígito verificador
5. ✅ Aceita com ou sem formatação

**Exemplos válidos**:
```python
contract.is_cpf("123.456.789-09", "cpf")  # ✅ Formatado
contract.is_cpf("12345678909", "cpf")      # ✅ Sem formatação
```

**Exemplos inválidos** (todos serão rejeitados):
```python
contract.is_cpf("111.111.111-11", "cpf")  # ❌ Sequencial
contract.is_cpf("000.000.000-00", "cpf")  # ❌ Todos zeros
contract.is_cpf("123.456.789-00", "cpf")  # ❌ Dígito verificador inválido
```

---

### is_cnpj(*value, field, message=IS_NOT_CNPJ*)

Valida se uma string é um CNPJ válido com verificação completa de dígitos verificadores.

```python
contract.is_cnpj("11.222.333/0001-81", "cnpj", "CNPJ inválido")
```

**Parâmetros**:

- *value ([str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/reference/datamodel.html#none))* - CNPJ a ser validado (com ou sem formatação).
- *field ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Nome do campo.
- *message ([str](https://docs.python.org/3/library/stdtypes.html#str))* - Opcional. Mensagem personalizada.
  - *IS_NOT_CNPJ* = "The field {0} must not be a valid CNPJ"

**Validações realizadas**:
1. ✅ Formato correto (14 dígitos)
2. ✅ Rejeita números sequenciais (11.111.111/1111-11, etc.)
3. ✅ Valida primeiro dígito verificador
4. ✅ Valida segundo dígito verificador
5. ✅ Aceita com ou sem formatação

**Exemplos válidos**:
```python
contract.is_cnpj("11.222.333/0001-81", "cnpj")  # ✅ Formatado
contract.is_cnpj("11222333000181", "cnpj")       # ✅ Sem formatação
```

**Exemplos inválidos** (todos serão rejeitados):
```python
contract.is_cnpj("11.111.111/1111-11", "cnpj")  # ❌ Sequencial
contract.is_cnpj("00.000.000/0000-00", "cnpj")  # ❌ Todos zeros
contract.is_cnpj("11.222.333/0001-00", "cnpj")  # ❌ Dígito verificador inválido
```

---

## Exemplo Completo

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

class CadastroPessoa(Notifiable):
    def __init__(self, nome, cpf, cnpj=None):
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.cnpj = cnpj

        contract = (
            Contract()
            .requires(self.nome, "nome", "Nome é obrigatório")
            .is_cpf(self.cpf, "cpf", "CPF inválido")
        )

        # Se for empresa, valida CNPJ
        if self.cnpj:
            contract.is_cnpj(self.cnpj, "cnpj", "CNPJ inválido")

        self.add_notifications(contract.get_notifications())

# Pessoa Física
pessoa = CadastroPessoa(
    nome="João Silva",
    cpf="123.456.789-09"  # CPF válido
)

if pessoa.is_valid:
    print("✅ Cadastro válido!")

# Empresa
empresa = CadastroPessoa(
    nome="Empresa XYZ LTDA",
    cpf="111.444.777-35",      # CPF do responsável
    cnpj="11.222.333/0001-81"  # CNPJ da empresa
)

if empresa.is_valid:
    print("✅ Empresa cadastrada com sucesso!")
else:
    for notification in empresa.get_notifications():
        print(f"❌ [{notification.field}] {notification.message}")
```

---

## Padrões Regex Disponíveis (Avançado)

Além das validações completas acima, o PyFlunt também fornece padrões regex para casos avançados:

### CPF (Cadastro de Pessoa Física)

**Padrão aceito**:
```regex
^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$
```

**Formatos válidos**:
```python
"123.456.789-10"  # Formatado
"12345678910"     # Sem formatação
"123.456.789-10"  # Com pontos e hífen
"12345678910"     # Apenas números
```

**Como usar o padrão**:
```python
from flunt.localization.flunt_regex_patterns import get_pattern
import re

cpf_pattern = get_pattern("cpf")
regex = re.compile(cpf_pattern)

# Validar formato
if regex.match("123.456.789-10"):
    print("✅ Formato válido")
else:
    print("❌ Formato inválido")
```

### CNPJ (Cadastro Nacional de Pessoa Jurídica)

**Padrão aceito**:
```regex
^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$
```

**Formatos válidos**:
```python
"12.345.678/0001-90"  # Formatado
"12345678000190"      # Sem formatação
"12.345.678/0001-90"  # Com pontos, barra e hífen
"12345678000190"      # Apenas números
```

**Como usar o padrão**:
```python
from flunt.localization.flunt_regex_patterns import get_pattern
import re

cnpj_pattern = get_pattern("cnpj")
regex = re.compile(cnpj_pattern)

# Validar formato
if regex.match("12.345.678/0001-90"):
    print("✅ Formato válido")
else:
    print("❌ Formato inválido")
```

---

## Algoritmo de Validação

O PyFlunt implementa os algoritmos oficiais de validação de CPF e CNPJ:

---

### Validação de CPF

**Passos do algoritmo**:
1. Remove formatação (mantém apenas dígitos)
2. Verifica se tem exatamente 11 dígitos
3. Rejeita sequências conhecidas (111.111.111-11, 000.000.000-00, etc.)
4. Calcula o primeiro dígito verificador
5. Calcula o segundo dígito verificador
6. Compara com os dígitos fornecidos

**Fórmula dos dígitos verificadores**:
- Primeiro dígito: `(soma * 10 % 11) % 10`
- Segundo dígito: `(soma * 10 % 11) % 10`

### Validação de CNPJ

**Passos do algoritmo**:
1. Remove formatação (mantém apenas dígitos)
2. Verifica se tem exatamente 14 dígitos
3. Rejeita sequências conhecidas
4. Calcula o primeiro dígito verificador com pesos [5,4,3,2,9,8,7,6,5,4,3,2]
5. Calcula o segundo dígito verificador com pesos [6,5,4,3,2,9,8,7,6,5,4,3,2]
6. Compara com os dígitos fornecidos

---

## Funcionalidades Implementadas

- ✅ Validação de formato (aceita com ou sem formatação)
- ✅ Validação de dígitos verificadores
- ✅ Rejeição de números sequenciais (111.111.111-11, etc.)
- ✅ Rejeição de números conhecidos como inválidos
- ✅ Suporte para CPF/CNPJ formatado e não formatado
- ✅ Mensagens de erro personalizáveis

---

## Outros Documentos Brasileiros (Futuro)

Além de CPF e CNPJ, estão planejados:

### CEP (Código de Endereçamento Postal)
```python
# Planejado
contract.is_cep(cep, "cep", "CEP inválido")
# Aceita: "12345-678" ou "12345678"
```

### Título de Eleitor
```python
# Planejado
contract.is_titulo_eleitor(titulo, "titulo", "Título de eleitor inválido")
```

### PIS/PASEP
```python
# Planejado
contract.is_pis(pis, "pis", "PIS inválido")
```

### CNH (Carteira Nacional de Habilitação)
```python
# Planejado
contract.is_cnh(cnh, "cnh", "CNH inválida")
```

---

## Todos os Padrões Disponíveis

Para acessar todos os padrões regex disponíveis:

```python
from flunt.localization.flunt_regex_patterns import REGEX_PATTERNS

# Ver todos os padrões
print(REGEX_PATTERNS)
# {
#     "email": "...",
#     "cpf": r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$",
#     "cnpj": r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$",
#     "url": "...",
#     ...
# }

# Obter padrão específico
from flunt.localization.flunt_regex_patterns import get_pattern

cpf_pattern = get_pattern("cpf")
cnpj_pattern = get_pattern("cnpj")
```

---

## Contribuindo

Quer ajudar a implementar validações de outros documentos brasileiros? Confira:

- 📋 [Issues do Projeto](https://github.com/fazedordecodigo/PyFlunt/issues)
- 📖 [Guia de Contribuição](https://github.com/fazedordecodigo/PyFlunt/blob/main/CONTRIBUTING.md)

Sua contribuição é muito bem-vinda! 🇧🇷
