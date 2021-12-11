"""Module Contract."""
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class BoolValidationContract(Notifiable):
    def is_false(self, value: bool, key: str, message: str):
        """Requires that a bool is false

        :param value
        :param key
        :param message

        :return
        """
        if value:
            self.add_notification(Notification(key, message))

        return self

    def is_true(self, value: bool, key: str, message: str):
        """Requires that a bool is true

        :param value
        :param key
        :param message

        :return
        """
        if not value:
            self.add_notification(Notification(key, message))

        return self
