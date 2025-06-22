"""Módulo de exemplo com Objetos de Valor."""

from __future__ import annotations

import logging
import time

from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)


logging.getLogger(__name__)


def time_me(function):  # type: ignore
    def wrap(*arg):  # type: ignore
        start = time.time()
        r = function(*arg)
        end = time.time()
        logging.info(f"{function.__name__} ({(end - start) * 1000:0.3f} ms)")
        return r

    return wrap


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
            .requires(self.primeiro_nome, "primeiro nome")
            .requires(self.ultimo_nome, "ultimo nome")
            .requires(self.email, "email", "E-mail é obrigatório")
            .is_lower_than(self.primeiro_nome, 50, "primeiro_nome")
            .is_lower_than(self.ultimo_nome, 50, "ultimo_nome")
            .is_greater_or_equals_than(self.primeiro_nome, 3, "primeiro_nome")
            .is_greater_or_equals_than(self.ultimo_nome, 3, "ultimo_nome")
            .is_email(self.email, "email", "E-mail é obrigatório")
            .is_email(self.email, "email", "E-mail inválido")
        )

        # Adicionando as notificações do contrato à entidade
        self.add_notifications(contract.get_notifications())


@time_me
def main() -> None:
    """Função principal de exemplo."""
    pessoa = Pessoa("Em", "Delatorre", "contato@delatorre.dev")
    for _i in range(1_000_000):
        if pessoa.is_valid:
            pass


if __name__ == "__main__":
    main()
