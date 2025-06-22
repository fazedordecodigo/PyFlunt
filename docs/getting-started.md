# Guia de Início Rápido

Este guia irá te mostrar os passos básicos para começar a usar o Pyflunt no seu projeto.

## 1. Instalação

Primeiro, instale a biblioteca usando `pip`:

```bash
pip install pyflunt
```

## 2\. O Conceito Principal: O `Contract`

O coração do Pyflunt é a classe `Contract`. Você a utiliza para definir as regras de validação para os seus dados.

A ideia é criar um "contrato" que seus dados devem seguir. Cada método de validação que você chama no contrato verifica uma regra. Se a regra for violada, uma `Notification` é adicionada à lista de notificações do contrato.

## 3\. Criando sua Primeira Validação

Vamos criar uma validação para um simples objeto `Pet`.

```python
from flunt.validations.contract import Contract

class Pet:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        self._validar()

    def _validar(self):
        contract = (
            Contract()
            .requires(self.nome, "Nome", "O nome do pet é obrigatório.")
            .is_lower_than(nome, 50, "Nome", "O nome do pet deve ser menor que 50 caracteres")
            .is_greater_than(self.idade, 0, "Idade", "A idade do pet deve ser maior que zero.")
        )
        # Você pode adicionar as notificações ao seu objeto de domínio
        self.notifications = contract.notifications
        self.is_valid = contract.is_valid

# --- Testando a validação ---

# Cenário 1: Dados Válidos
pet_valido = Pet("Bolinha", 5)
print(f"'{pet_valido.nome}' é válido? {pet_valido.is_valid}")
# Saída: 'Bolinha' é válido? True

print("-" * 20)

# Cenário 2: Dados Inválidos
pet_invalido = Pet("", -1)
print(f"Pet inválido é válido? {pet_invalido.is_valid}")
print("Notificações de erro:")
for notificacao in pet_invalido.notifications:
    print(f"- Campo: '{notificacao.field}', Mensagem: '{notificacao.message}'")
```

```
Saída:
'Bolinha' é válido? True
--------------------
Pet inválido é válido? False
Notificações de erro:
- Campo: 'Nome', Mensagem: 'O nome do pet é obrigatório.'
- Campo: 'Idade', Mensagem: 'A idade do pet deve ser maior que zero.'
```

## 4\. Verificando o Resultado

Após definir o contrato, você pode verificar se os dados são válidos usando a propriedade `is_valid`.

  - `contract.is_valid`: Retorna `True` se nenhuma notificação de erro foi adicionada, e `False` caso contrário.
  - `contract.notifications`: É uma lista contendo todos os objetos `Notification` gerados pelas regras que falharam.

Com isso, você pode separar a lógica de validação da lógica de tratamento de erros, deixando seu código mais limpo e alinhado aos princípios do Domain-Driven Design (DDD).
