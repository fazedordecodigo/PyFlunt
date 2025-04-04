"""Módulo de exemplo com Objetos de Valor."""

from __future__ import annotations

import logging

from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract


class Pessoa(Notifiable):
    """Classe Objeto de Valor Pessoa."""

    def __init__(
        self, primeiro_nome: str, ultimo_nome: str, email: str
    ) -> None:
        """Construtor da classe."""
        super().__init__()
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.email = email

        # Criando um contrato de validação
        contract = (
            Contract()
            .requires(
                self.primeiro_nome, "primeiro nome", "Nome é obrigatório"
            )
            .requires(
                self.ultimo_nome, "ultimo nome", "Sobrenome é obrigatório"
            )
            .requires(self.email, "email", "E-mail é obrigatório")
            .is_lower_than(
                self.primeiro_nome,
                3,
                "primeiro_nome",
                "Nome deve ter no mínimo 3 caracteres",
            )
            .is_lower_than(
                self.ultimo_nome,
                3,
                "ultimo_nome",
                "Sobrenome deve ter no mínimo 3 caracteres",
            )
            .is_email(self.email, "email", "E-mail inválido")
        )

        # Adicionando as notificações do contrato à entidade
        self.add_notifications(contract.get_notifications())


def main() -> None:
    """Função principal de exemplo."""
    pessoa = Pessoa("Emerson", "Delatorre", "emerson@delatorre.dev")
    if not pessoa.is_valid:
        for notification in pessoa.get_notifications():
            logging.info(notification)
    else:
        logging.info("Validado com sucesso!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
