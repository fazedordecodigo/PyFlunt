# Validações de Documentos Brasileiros

PyFlunt oferece suporte para validação de documentos brasileiros, com foco em CPF e CNPJ.

!!! warning "Funcionalidade em Desenvolvimento"
    Atualmente, as validações de CPF e CNPJ verificam apenas o **formato** (quantidade de dígitos e caracteres especiais), mas **não validam os dígitos verificadores**. A validação completa está planejada para uma próxima versão ([#29](https://github.com/fazedordecodigo/PyFlunt/issues/29)).

---

## Padrões Regex Disponíveis

Atualmente, o PyFlunt fornece padrões regex para validação de formato:

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

## Limitações Atuais

!!! danger "Importante: Validação Incompleta"
    **A validação atual NÃO verifica os dígitos verificadores!**

    Isso significa que documentos com formato correto mas dígitos inválidos passarão pela validação:

    ```python
    # ❌ Estes CPFs/CNPJs INVÁLIDOS passariam na validação atual:
    "111.111.111-11"  # CPF sequencial (inválido)
    "000.000.000-00"  # CPF com zeros (inválido)
    "12.345.678/0001-00"  # CNPJ com dígitos verificadores errados
    ```

### Por que isso importa?

Os dígitos verificadores são calculados através de um algoritmo específico e servem para:

1. **Detectar erros de digitação**
2. **Validar autenticidade** do documento
3. **Prevenir números sequenciais** inválidos

Sem essa validação, seu sistema pode aceitar documentos falsos ou inválidos.

---

## Validação Temporária (Workaround)

Enquanto a validação completa não está implementada, você pode usar bibliotecas externas:

### Opção 1: Usando `validate-docbr`

```bash
pip install validate-docbr
```

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract
from validate_docbr import CPF, CNPJ

class PessoaBrasileira(Notifiable):
    def __init__(self, cpf, cnpj=None):
        super().__init__()
        self.cpf = cpf
        self.cnpj = cnpj

        # Validadores externos
        cpf_validator = CPF()
        cnpj_validator = CNPJ()

        # Contract do PyFlunt
        contract = Contract()

        # Validar CPF (com dígitos verificadores)
        if self.cpf and not cpf_validator.validate(self.cpf):
            contract.add_notification("cpf", "CPF inválido")

        # Validar CNPJ (se fornecido)
        if self.cnpj and not cnpj_validator.validate(self.cnpj):
            contract.add_notification("cnpj", "CNPJ inválido")

        self.add_notifications(contract.get_notifications())

# Uso
pessoa = PessoaBrasileira(cpf="123.456.789-10")  # CPF inválido
if not pessoa.is_valid:
    for notification in pessoa.get_notifications():
        print(f"❌ {notification.message}")
```

### Opção 2: Implementação Manual

```python
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

def validar_cpf(cpf: str) -> bool:
    """Valida CPF com dígitos verificadores."""
    # Remove formatação
    cpf = ''.join(filter(str.isdigit, cpf))

    # CPF deve ter 11 dígitos
    if len(cpf) != 11:
        return False

    # CPFs conhecidos como inválidos
    if cpf in [
        '00000000000', '11111111111', '22222222222',
        '33333333333', '44444444444', '55555555555',
        '66666666666', '77777777777', '88888888888',
        '99999999999'
    ]:
        return False

    # Validar primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    if int(cpf[9]) != digito1:
        return False

    # Validar segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    if int(cpf[10]) != digito2:
        return False

    return True


def validar_cnpj(cnpj: str) -> bool:
    """Valida CNPJ com dígitos verificadores."""
    # Remove formatação
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # CNPJ deve ter 14 dígitos
    if len(cnpj) != 14:
        return False

    # CNPJs conhecidos como inválidos
    if cnpj in [
        '00000000000000', '11111111111111', '22222222222222',
        '33333333333333', '44444444444444', '55555555555555',
        '66666666666666', '77777777777777', '88888888888888',
        '99999999999999'
    ]:
        return False

    # Validar primeiro dígito verificador
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos1[i] for i in range(12))
    digito1 = 11 - (soma % 11)
    digito1 = 0 if digito1 >= 10 else digito1

    if int(cnpj[12]) != digito1:
        return False

    # Validar segundo dígito verificador
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos2[i] for i in range(13))
    digito2 = 11 - (soma % 11)
    digito2 = 0 if digito2 >= 10 else digito2

    if int(cnpj[13]) != digito2:
        return False

    return True


class Empresa(Notifiable):
    """Exemplo de uso com validação manual."""

    def __init__(self, cnpj, cpf_responsavel):
        super().__init__()
        self.cnpj = cnpj
        self.cpf_responsavel = cpf_responsavel

        contract = Contract()

        # Validar CNPJ
        if not validar_cnpj(self.cnpj):
            contract.add_notification("cnpj", "CNPJ inválido")

        # Validar CPF do responsável
        if not validar_cpf(self.cpf_responsavel):
            contract.add_notification("cpf_responsavel", "CPF do responsável inválido")

        self.add_notifications(contract.get_notifications())


# Teste
empresa = Empresa(
    cnpj="11.222.333/0001-81",  # CNPJ válido
    cpf_responsavel="111.111.111-11"  # CPF inválido (sequencial)
)

if not empresa.is_valid:
    for notification in empresa.get_notifications():
        print(f"❌ [{notification.field}] {notification.message}")
```

---

## Roadmap - Próxima Versão

A próxima versão do PyFlunt incluirá métodos nativos para validação completa:

```python
# 🚀 API planejada para próxima versão
from flunt.validations.contract import Contract

contract = (
    Contract()
    # Validar CPF com dígitos verificadores
    .is_cpf(cpf, "cpf", "CPF inválido")

    # Validar CNPJ com dígitos verificadores
    .is_cnpj(cnpj, "cnpj", "CNPJ inválido")

    # Validar CPF ou CNPJ
    .is_cpf_or_cnpj(documento, "documento", "Documento inválido")
)
```

**Funcionalidades planejadas**:

- ✅ Validação de formato (já existe)
- ⏳ Validação de dígitos verificadores
- ⏳ Rejeição de números sequenciais (`111.111.111-11`)
- ⏳ Rejeição de números conhecidos como inválidos
- ⏳ Suporte para formatado e não formatado
- ⏳ Máscaras automáticas (formatação)

Acompanhe o progresso: [Issue #29](https://github.com/fazedordecodigo/PyFlunt/issues/29)

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

Quer ajudar a implementar validações completas de CPF/CNPJ? Confira:

- 📋 [Issue #29 - Validação de Documentos](https://github.com/fazedordecodigo/PyFlunt/issues/29)
- 📖 [Guia de Contribuição](https://github.com/fazedordecodigo/PyFlunt/blob/main/CONTRIBUTING.md)

Sua contribuição é muito bem-vinda! 🇧🇷
