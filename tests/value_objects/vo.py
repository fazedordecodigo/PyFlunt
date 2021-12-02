"""Module Value Objects."""
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract


class Name(Notifiable):
    """Class Value Object Name."""

    def __init__(self, first_name: str, last_name: str) -> None:
        """Found 'Constructor'."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

        self.contract = (
            Contract()
            .requires(self.first_name, "first name")
            .requires(self.last_name, "last name")
            .has_min_len(
                value=self.first_name,
                minimum=3,
                field="first_name",
                message="Mínimo de 3 caracteres",
            )
            .has_max_len(
                value=self.first_name,
                maximum=50,
                field="first_name",
                message="Máximo de 50 caracteres",
            )
            .has_min_len(
                value=self.last_name,
                minimum=3,
                field="last_name",
                message="Mínimo de 3 caracteres",
            )
            .has_max_len(
                value=self.last_name,
                maximum=50,
                field="last_name",
                message="Máximo de 50 caracteres",
            )
        )

        self.add_notifications_of_contract(self.contract)


class Email(Notifiable):
    """Class Value Object E-mail."""

    def __init__(self, address: str) -> None:
        """Found 'Constructor'."""
        super().__init__()
        self.address = address

        self.contract = (
            Contract()
            .requires(self.address, "E-mail address")
            .is_email(
                self.address,
                "address",
                "Este Campo aceita apenas texto no formato e-mail",
            )
        )

        self.add_notifications_of_contract(self.contract)
