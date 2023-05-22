"""Module Notifiable."""
from interface import Interface

from flunt.notifications.notification import Notification


class INotifiable(Interface):
    """Interface Notifiable."""

    def add_notification(self, notification: Notification):
        """Add a new notification.

        :param notification: Notification
        """
        pass
