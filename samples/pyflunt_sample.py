from pyflunt.notifiable import Notifiable
from pyflunt.contract import Contract


class Email(Notifiable):
    def __init__(self, email):
        super().__init__()

        self._email = email

        contract = (
            Contract()
            .requires()
            .has_max_len(
                value=email,
                maximum=50,
                message='invalid email'
            )
            .is_email(
                value=email,
                field='email',
                message='invalid email'
            )
        )

        self.add_notifications(contract)
