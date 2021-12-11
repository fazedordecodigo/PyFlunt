"""Module Contract."""
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification
from flunt.validations.strings import StringValidationContract
from flunt.validations.email import EmailValidationContract
from flunt.validations.bool import BoolValidationContract


class Contract(
    StringValidationContract,
    EmailValidationContract,
    BoolValidationContract,
    Notifiable
):
    def requires(self, value: str, key: str):
        """Require.

        :param value
        :param key

        :return
        """
        if not value:
            self.add_notification(
                Notification(key, "Campo preenchimento obrigatório")
            )

        return self.is_non
