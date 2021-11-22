"""Module Notifiable."""
from flunt.notification import Notification


class Notifiable(Notification):
    """Class Notifiable."""

    def __init__(self) -> None:
        """Found 'Constructor'."""
        self._notifications: list = []

    def add_notification(self, notification: Notification):
        """Add a new notification.

        :param notification: Notification
        """
        self._notifications.append(notification)

    def add_notifications_of_contract(self, *notifications):
        """Add notification of contract object."""
        self._notifications += self._filter_and_map_notifiables(notifications)

    def _filter_and_map_notifiables(self, notifications):
        return [
            notification
            for notifiable in notifications
            if isinstance(notifiable, Notifiable)
            for notification in notifiable._notifications
        ]

    def _filter_notifications(self, notifications):
        return [
            notification
            for notification in notifications
            if isinstance(notification, Notification)
        ]

    def get_notifications(self) -> list:
        """Get all notifications.

        :return: list
        """
        return self._notifications

    def clear(self):
        """Clear all existing notifications."""
        self._notifications.clear()

    def is_valid(self) -> bool:
        """Return if notifiable is valid, if not notified.

        :return: bool
        """
        if len(self._notifications) <= 0:
            return True
        return False

    def __str__(self):
        """Print object string."""
        return self._notifications.__str__()
