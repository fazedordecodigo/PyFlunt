"""Module Notifiable."""

from abc import ABC

from flunt.notifications.notification import Notification


class Notifiable(ABC):  # noqa: B024
    """
    A class representing an object that can be notified.

    This class extends Notification and provides methods for managing notifications.

    Attributes
    ----------
    notifications: list[Notification]
            A list of notifications.
    is_valid: bool
            A boolean indicating if there are any notifications.

    Methods
    -------
    - get_notification_instance
    - add_notifications
    - add_notification
    - get_notifications
    - clear

    """

    def __init__(self) -> None:
        """Initialize the list of notifications."""
        self._notifications: list[Notification] = []

    @property
    def notifications(self) -> list[Notification]:
        """
        Return the list of notifications.

        Returns
        -------
        `list[Notification]`
                A list of notifications.

        Examples
        --------
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

        Returns
        -------
        `bool`
                True if there are no notifications, False otherwise.

        Examples
        --------
        ```python
        obj = Notifiable()
        obj.is_valid()  # True
        ```

        """
        return not self._notifications

    def add_notifications(self, notifications: list[Notification]) -> None:
        """
        Add notifications from a list of contracts to the list of notifications.

        Parameters
        ----------
        `notifications`: list[Notification]
                A list of notifications to be added.

        Returns
        -------
        `None`

        Examples
        --------
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

        Parameters
        ----------
        `notification`: Notification
                The notification to be added.

        Returns
        -------
        `None`

        Examples
        --------
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

        Returns
        -------
        `list[Notification]`
                A list of notifications.

        Examples
        --------
        ```python
        obj = Notifiable()
        obj.get_notifications()  # []
        ```

        """
        return self._notifications

    def clear(self) -> None:
        """
        Clear the list of notifications.

        Returns
        -------
        `None`

        Examples
        --------
        ```python
        obj = Notifiable()
        obj.clear()  # []
        ```

        """
        self._notifications.clear()

    def __repr__(self) -> str:
        """
        Return a string representation of the list of notifications.

        Returns
        -------
        `str`
                A string representation of the list of notifications.

        Examples
        --------
        ```python
        obj = Notifiable()
        repr(obj)  # "[]"
        ```

        """
        return repr(self._notifications)
