"""Module Contract."""
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class StringValidationContract(Notifiable):
    """Class Contract."""

    def is_lower_than(self, value: str, compare: int, key: str, message: str):
        """Requires a string len is lower than

        :param value
        :param compare
        :param key
        :param message

        :return
        """
        if not value:
            return self

        if len(value) >= compare:
            self.add_notification(Notification(key, message))

        return self

    def is_lower_or_equals_than(
        self,
        value: str,
        compare: int,
        key: str,
        message: str
    ):
        """Requires a string len is lower or equals than

        :param value
        :param compare
        :param key
        :param message

        :return
        """
        if not value:
            return self

        if len(value) > compare:
            self.add_notification(Notification(key, message))

        return self

    def is_greater_than(
        self,
        value: str,
        comparer: int,
        key: str,
        message: str
    ):
        """Requires a string is greater than.

        :param value
        :param comparer
        :param key
        :param message

        :return
        """
        if not value:
            return self

        if len(value) <= comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_greater_or_equals_than(
        self,
        value: str,
        comparer: int,
        key: str,
        message: str
    ):
        """Requires a string len is greater or equals than

        :param value
        :param comparer
        :param key
        :param message

        :return: self
        """
        if not value:
            return self

        if len(value) < comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_none(self, value: str, key: str, message: str):
        """Requires a string is not none

        :param value
        :param key
        :param message

        :return
        """
        if value is not None:
            self.add_notification(Notification(key, message))

        return self

    def is_not_none(self, value: str, key: str, message: str):
        """Requires a string is not none

        :param value
        :param key
        :param message

        :return
        """
        if value is None:
            self.add_notification(Notification(key, message))

        return self

    def is_not_none_or_white_space(self, value: str, key: str, message: str):
        """Requires a string is not null or white space

        :param value
        :param key
        :param message

        :return
        """
        if value is None or value.isspace():
            self.add_notification(Notification(key, message))

        return self

    def are_equals(self, value: str, compare: str, key: str, message: str):
        """Requires two strings are equals

        :param value
        :param key
        :param message

        :return
        """
        if value != compare:
            self.add_notification(Notification(key, message))

        return self

    def are_not_equals(self, value: str, compare: str, key: str, message: str):
        """Requires two strings are not equals

        :param value
        :param key
        :param message

        :return
        """
        if value == compare:
            self.add_notification(Notification(key, message))

        return self

    def contains(self, value: str, compare: str, key: str, message: str):
        """Requires a string contains

        :param value
        :param key
        :param message

        :return
        """

        if value.find(compare) > -1:
            self.add_notification(Notification(key, message))

        return self

    def not_contains(self, value: str, compare: str, key: str, message: str):
        """Requires a string not contains

        :param value
        :param key
        :param message

        :return
        """

        if value.find(compare) == -1:
            self.add_notification(Notification(key, message))

        return self
