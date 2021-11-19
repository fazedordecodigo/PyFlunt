"""Module Contract."""
from flunt.notification import Notification
from flunt.notifiable import Notifiable
import re


class Contract(Notifiable):
    """Class Contract."""

    def has_min_len(self, value, minimum, field, message):
        """Minimum length.

        :param value: attribute
        :param minimum: int
        :param field: str
        :param message: str

        :return: self
        """
        if not value or len(value) < minimum:
            self.add_notification(
                Notification(field, message)
            )

        return self

    def is_email(self, value, field, message):
        """Check if it's email.

        :param value: attribute
        :param field: str
        :param message: str

        :return: self
        """
        if not self._valid_email(value):
            self.add_notification(
                Notification(field, message)
            )

        return self

    def _valid_email(self, value):
        return re.match(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
            value,
            re.IGNORECASE
        )

    def requires(self, value, field):
        """Require.

        :param value: attribute
        :param field: str

        :return: self
        """
        if not value:
            self.add_notification(
                Notification(field, 'Campo preenchimento obrigatório')
            )

        return self
