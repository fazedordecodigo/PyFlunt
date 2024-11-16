"""Module Value Objects."""
from __future__ import annotations

from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract


class Name(Notifiable):
    """Value Object Name."""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Found 'Constructor'."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.add_notifications(
            Contract()
            .requires(self.first_name, "first name", "Nome é obrigatório")
            .requires(self.last_name, "last name", "Sobrenome é obrigatório")
            .is_between(
                self.first_name,
                3,
                50,
                "first_name",
                "Mínimo de 3 e máximo de 50 caracteres",
            )
            .is_between(
                self.last_name,
                3,
                50,
                "last_name",
                "Mínimo de 3 e máximo de 50 caracteres",
            )
            .get_notifications()
        )


class Email(Notifiable):
    """Class Value Object E-mail."""

    def __init__(self, address: str) -> None:
        """Found 'Constructor'."""
        super().__init__()
        self.address = address

        self.add_notifications(
            Contract()
            .requires(self.address, "E-mail address", "E-mail é obrigatório")
            .is_email(
                self.address,
                "address",
                "Este Campo aceita apenas texto no formato e-mail",
            )
            .get_notifications()
        )
