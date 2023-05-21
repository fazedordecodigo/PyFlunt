"""Module Contract."""
import re

from flunt.localization.flunt_regex_patterns import FluntRegexPatterns
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class EmailValidationContract(Notifiable):
    """Class Email Validation Contract."""

    def is_email(self, value: str, key: str, message: str):
        """Require a string is an email.

        :param value
        :param key
        :param message

        :return
        """
        if not self._valid_email(value):
            self.add_notification(Notification(key, message))

        return self

    def is_not_email(self, value: str, key: str, message: str):
        """Require a string is not an email.

        :param value
        :param key
        :param message

        :return
        """
        if self._valid_email(value):
            self.add_notification(Notification(key, message))

        return self

    def _valid_email(self, value):
        return re.match(
            FluntRegexPatterns().email_regex_pattern,
            value,
            re.IGNORECASE,
        )
