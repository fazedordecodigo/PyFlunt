"""Module Value Objects."""
from flunt.notifiable import Notifiable
from flunt.contract import Contract


class Name(Notifiable):
    """Class Value Object Name."""

    def __init__(self, first_name, last_name):
        """Found 'Constructor'."""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

        self.contract = (
            Contract()
            .requires(self.first_name, 'first name')
            .requires(self.last_name, 'last name')
            .has_min_len(
                value=self.first_name,
                minimum=3,
                field='first_name',
                message='Mínimo de 3 caracteres'
            )
            .has_min_len(
                value=self.last_name,
                minimum=3,
                field='last_name',
                message='Mínimo de 3 caracteres'
            )
        )

        self.add_notifications_of_contract(self.contract)
