"""Module Contract."""
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification
from flunt.validations.bool_validation_contract import BoolValidationContract
from flunt.validations.email_validation_contract import EmailValidationContract
from flunt.validations.strings_validation_contract import (
    StringValidationContract,
)


class Contract(
    StringValidationContract,
    EmailValidationContract,
    BoolValidationContract,
    Notifiable,
):
    """Class Contract."""

    def requires(self, value: str, key: str):
        """Require.

        :param value
        :param key

        :return
        """
        if not value:
            self.add_notification(
                Notification(key, 'Campo preenchimento obrigatório')
            )

        return self
