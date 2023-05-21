"""Module Contract."""
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class StringValidationContract(Notifiable):
    """Class String Validation Contract."""

    def is_lower_than(self, value: str, comparer: int, key: str, message: str):
        """Require a string len is lower than.

        :param value
        :param comparer
        :param key
        :param message

        :return
        """
        if not value:
            return self

        if len(value) > comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_lower_or_equals_than(
        self,
        value: str,
        comparer: int,
        key: str,
        message: str
    ):
        """Require a string len is lower or equals than.

        :param value
        :param comparer
        :param key
        :param message

        :return
        """
        if not value:
            return self

        if len(value) >= comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_greater_than(
        self,
        value: str,
        comparer: int,
        key: str,
        message: str
    ):
        """Require a string is greater than.

        :param value
        :param comparer
        :param key
        :param message

        :return
        """
        if not value:
            return self

        if len(value) < comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_greater_or_equals_than(
        self,
        value: str,
        comparer: int,
        key: str,
        message: str
    ):
        """Require a string len is greater or equals than.

        :param value
        :param comparer
        :param key
        :param message

        :return: self
        """
        if not value:
            return self

        if len(value) <= comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_none(self, value: str, key: str, message: str):
        """Require a string is not none.

        :param value
        :param key
        :param message

        :return
        """
        if value is not None:
            self.add_notification(Notification(key, message))

        return self

    def is_not_none(self, value: str, key: str, message: str):
        """Require a string is not none.

        :param value
        :param key
        :param message

        :return
        """
        if value is None:
            self.add_notification(Notification(key, message))

        return self

    def is_not_none_or_white_space(self, value: str, key: str, message: str):
        """Require a string is not null or white space.

        :param value
        :param key
        :param message

        :return
        """
        if value is None or value.isspace():
            self.add_notification(Notification(key, message))

        return self

    def are_equals(self, value: str, comparer: str, key: str, message: str):
        """Require two strings are equals.

        :param value
        :param comparer
        :param key
        :param message

        :return
        """
        if value != comparer:
            self.add_notification(Notification(key, message))

        return self

    def are_not_equals(self, value: str, comparer: str, key: str, message: str):
        """Require two strings are not equals.

        :param value
        :param comparer
        :param key
        :param message

        :return
        """
        if value == comparer:
            self.add_notification(Notification(key, message))

        return self

    def contains(self, value: str, comparer: str, key: str, message: str):
        """Require a string contains.

        :param value
        :param comparer
        :param key
        :param message

        :return
        """
        if value.find(comparer) > -1:
            self.add_notification(Notification(key, message))

        return self

    def not_contains(self, value: str, comparer: str, key: str, message: str):
        """Require a string not contains.

        :param value
        :param comparer
        :param key
        :param message

        :return
        """
        if value.find(comparer) == -1:
            self.add_notification(Notification(key, message))

        return self
    
    def is_between(self, value: str, min: int, max: int, key: str, message: str):
        """Requires a string len is between.

        :param value
        :param min
        :param max
        :param key
        :param message

        :return
        """
        if not value:
            return self

        if value is None or value.isspace():
            return self

        if len(value) < min or len(value) > max:
            self.add_notification(Notification(key, message))

        return self
