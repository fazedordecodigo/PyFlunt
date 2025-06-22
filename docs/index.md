# Bem-vindo ao Pyflunt

![Logo do projeto](assets/pyflunt.png)

**Pyflunt** é uma biblioteca Python leve e poderosa para criar validações de domínio de forma fluente e expressiva, inspirada no *Domain Notification Pattern*.

Ela ajuda você a parar de usar exceções para controle de fluxo de validação e a começar a trabalhar com um modelo de domínio mais rico e resiliente, que acumula notificações de erro em vez de falhar no primeiro problema encontrado.

## Principais Características

* **API Fluente:** Escreva validações de forma legível e encadeada.
* **Sem Exceções:** Agregue todas as falhas de validação em uma lista de notificações.
* **Extensível:** Crie suas próprias regras de validação personalizadas com facilidade.
* **Leve e sem dependências:** Fácil de adicionar a qualquer projeto.

## Instalação

```bash
pip install flunt
```

## Exemplo Rápido

```python
from flunt.validations.contract import Contract
from flunt.notifications.notification import Notification

def registrar_usuario(nome, email):
    contract = (
        Contract()
        .requires(nome, "Nome", "O nome é obrigatório")
        .is_lower_than(nome, 50, "Nome", "O nome deve ser menor que 50 caracteres")
        .is_email(email, "Email", "O e-mail fornecido não é válido")
    )

    if not contract.is_valid:
        # Lida com as notificações (ex: retorna um erro 400 Bad Request)
        for notificacao in contract.notifications:
            print(f"- {notificacao.message}")
        return

    # Prossiga com a lógica de negócio...
    print("Usuário válido!")

# Exemplo de uso
registrar_usuario("Jo", "email_invalido")
```

```
Saída:
- O nome deve ter pelo menos 3 caracteres
- O e-mail fornecido não é válido
```

[Comece a usar agora\!](getting-started.md)
