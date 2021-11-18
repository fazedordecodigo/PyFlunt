"""Module Notifiable."""
from notification import Notification


class Notifiable(Notification):
    """Class Notifiable."""

    def __init__(self) -> None:
        """Found 'Constructor'."""
        self.__notification: list = []

    def add_notification(self, notification: Notification):
        """Add a new notification.

        :param notification: Notification
        """
        self.__notification.append(notification)

    def get_notifications(self) -> str:
        """Get all notifications.

        :return: string
        """
        msg = ''
        for notification in self.__notification:
            msg = msg + notification.message + '\n'
        return msg

    def clear(self):
        """Clear all existing notifications."""
        self.__notification.clear()

    def is_valid(self) -> bool:
        """Return if notifiable is valid, if not notified.

        :return: bool
        """
        if len(self.__notification) <= 0:
            return True
        return False
