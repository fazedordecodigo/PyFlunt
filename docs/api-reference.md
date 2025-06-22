# Referência da API

Esta seção fornece detalhes técnicos sobre as principais classes públicas do Pyflunt.

## A Classe `Contract`

A classe `Contract` é o ponto de entrada para todas as validações.

### Propriedades

-   **`notifications`**: `list[Notification]`
    Uma lista que armazena todas as notificações de erro geradas pelas validações que falharam. Se nenhuma validação falhar, a lista estará vazia.

-   **`is_valid`**: `bool`
    Uma propriedade somente leitura que retorna `True` se a lista `notifications` estiver vazia, e `False` caso contrário.

### Métodos

Todos os métodos de validação (ex: `requires`, `is_email`, etc.) retornam a própria instância de `Contract`, permitindo o encadeamento de chamadas (interface fluente).

## A Classe `Notification`

A classe `Notification` representa um único erro de validação.

### Propriedades

-   **`field`**: `str`
    O nome do campo que foi validado.

-   **`message`**: `str`
    A mensagem de erro descritiva.
