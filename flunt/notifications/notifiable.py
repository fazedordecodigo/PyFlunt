"""Module Notifiable."""

from __future__ import annotations

from flunt.notifications.notification import Notification
from flunt.protocols.notifiable_protocol import NotifiableProtocol


class Notifiable(NotifiableProtocol):
    """
    A class representing an object that can be notified.

    This class extends Notification and provides methods for managing notifications.

    Attributes:
        notifications (list[Notification]): A list of notifications.
        is_valid (bool): A boolean indicating if there are any notifications.

    """

    __slots__ = ("_notifications",)

    def __init__(self) -> None:
        """Initialize the list of notifications."""
        self._notifications: list[Notification] = []

    @property
    def notifications(self) -> list[Notification]:
        """
        Return the list of notifications.

        Returns:
            list[Notification]: A list of notifications.

        Examples:
            ```python
            obj = Notifiable()
            obj.notifications  # []
            ```

        """
        return self._notifications

    @property
    def is_valid(self) -> bool:
        """
        Check if there are any notifications.

        Returns:
            bool: True if there are no notifications, False otherwise.

        Examples:
            ```python
            obj = Notifiable()
            obj.is_valid  # True
            ```

        """
        return not self._notifications

    def add_notifications(self, notifications: list[Notification]) -> None:
        """
        Add notifications from a list of contracts to the list of notifications.

        Args:
            notifications (list[Notification]): A list of notifications to be added.

        Examples:
            ```python
            obj = Notifiable()
            obj.add_notifications([Notification("key", "message")])
            obj.notifications  # [Notification("key", "message")]
            ```

        """
        self._notifications.extend(notifications)

    def add_notification(self, field: str, message: str) -> None:
        """
        Add a single notification to the list of notifications.

        Args:
            field (str): The field or key for the notification.
            message (str): The message content of the notification.

        Examples:
            ```python
            obj = Notifiable()
            obj.add_notification("field", "message")
            obj.notifications  # [Notification("field", "message")]
            ```

        """
        self._notifications.append(Notification(field, message))

    def get_notifications(self) -> list[Notification]:
        """
        Return the list of notifications.

        Returns:
            list[Notification]: A list of notifications.

        Examples:
            ```python
            obj = Notifiable()
            obj.get_notifications()  # []
            ```

        """
        return self._notifications

    def clear(self) -> None:
        """
        Clear the list of notifications.

        Examples:
            ```python
            obj = Notifiable()
            obj.clear()  # []
            ```

        """
        self._notifications.clear()

    def __repr__(self) -> str:
        """Return the string representation of the list of notifications."""
        return repr(self._notifications)

    def __str__(self) -> str:
        """Return the string representation of the list of notifications."""
        return str(self._notifications)
