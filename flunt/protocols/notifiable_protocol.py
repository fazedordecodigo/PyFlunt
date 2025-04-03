"""Module Notifiable."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flunt.notifications.notification import Notification


class NotifiableProtocol(ABC):
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
    - add_notifications
    - add_notification
    - get_notifications
    - clear

    """

    @abstractmethod
    def __init__(self) -> None:
        """Initialize the list of notifications."""

    @property
    @abstractmethod
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

    @property
    @abstractmethod
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

    @abstractmethod
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

    @abstractmethod
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

    @abstractmethod
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

    @abstractmethod
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
