"""Module Contract."""
import re

from flunt.notifiable import Notifiable
from flunt.notification import Notification


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
            self.add_notification(Notification(field, message))

        return self

    def has_max_len(self, value, maximum, field, message):
        """Maximum length.

        :param value: attribute
        :param maximum: int
        :param field: str
        :param message: str

        :return: self
        """
        if not value or len(value) > maximum:
            self.add_notification(Notification(field, message))

        return self

    def is_email(self, value, field, message):
        """Check if it's email.

        :param value: attribute
        :param field: str
        :param message: str

        :return: self
        """
        if not self._valid_email(value):
            self.add_notification(Notification(field, message))

        return self

    def _valid_email(self, value):
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(regex, value, re.IGNORECASE)

    def requires(self, value, field):
        """Require.

        :param value: attribute
        :param field: str

        :return: self
        """
        if not value:
            self.add_notification(
                Notification(field, "Campo preenchimento obrigatório")
            )

        return self

    def is_false(self, value, field, message):
        """Check if It's False.

        :param value: attribute
        :param field: str
        :param message: str

        :return: self
        """
        if value:
            self.add_notification(Notification(field, message))

        return self

    def is_true(self, value, field, message):
        """Check if It's true.

        :param value: attribute
        :param field: str
        :param message: str

        :return: self
        """
        if not value:
            self.add_notification(Notification(field, message))

        return self

    def is_not_none(self, value, field, message):
        """Check if It's not None.

        :param value: attribute
        :param field: str
        :param message: str

        :return: self
        """
        if value is None:
            self.add_notification(Notification(field, message))

        return self

    def is_none(self, value, field, message):
        """Check if It's None.

        :param value: attribute
        :param field: str
        :param message: str

        :return: self
        """
        if value is not None:
            self.add_notification(Notification(field, message))

        return self
