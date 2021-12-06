"""Module Value Objects."""
from flunt.notifications.notifiable import Notifiable
from flunt.validations.contract import Contract


class Pessoa(Notifiable):
    """Class Value Object Name."""

    def __init__(self, first_name, last_name, email):
        """Found 'Constructor'."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        self.contract = (
            Contract()
            .requires(self.first_name, "first name")
            .requires(self.last_name, "last name")
            .requires(self.email, "e-mail")
            .has_min_len(
                value=self.first_name,
                minimum=3,
                field="first_name",
                message="Mínimo de 3 caracteres",
            )
            .has_min_len(
                value=self.last_name,
                minimum=3,
                field="last_name",
                message="Mínimo de 3 caracteres",
            )
            .is_email(value=self.email, field="email", message="email errado")
        )

        self.add_notifications_of_contract(self.contract)


def main():
    nome = Pessoa("Emerson", "Delatorre", "emersondelatorre.dev")
    if not nome.is_valid():
        for notification in nome.get_notifications():
            print(notification)
    else:
        print("sem notificações")


if __name__ == "__main__":
    main()
