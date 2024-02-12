"""Module Notifiable."""

from flunt.notifications.notification import Notification


class Notifiable(Notification):
    """
    A class representing an object that can be notified.

    This class extends Notification and provides methods for managing notifications.

    Attributes
    ----------
    _notifications: list[Notification]
        A list to store notifications.

    Methods
    -------
    __init__ -> None
        Initializes the Notifiable object.
    add_notification -> None
        Adds a single notification to the list of notifications.
    add_notifications_of_contract -> None
        Adds notifications from a list of contracts to the list of notifications.
    _filter_and_map_notifiables -> list[Notification]
        Filters and maps notifications from notifiable objects.
    _filter_notifications -> list[Notification]
        Filters notifications to ensure they are instances of Notification.
    get_notifications -> list[Notification]
        Returns the list of notifications.
    clear -> None
        Clears the list of notifications.
    is_valid -> bool
        Checks if there are any notifications.
    __str__ -> str
        Returns a string representation of the list of notifications.

    """

    def __init__(self) -> None:
        """Initialize the Notifiable object."""
        self._notifications: list[Notification] = []

    def add_notification(self, notification: Notification):
        """
        Add a single notification to the list of notifications.

        Parameters
        ----------
        notification: Notification
            The notification to be added.

        Returns
        -------
        None

        Examples
        --------
        >>> obj = Notifiable()

        >>> obj.add_notification(Notification("key", "message"))

        """
        self._notifications.append(notification)

    def add_notifications_of_contract(self, notifications: list[Notification]):
        """
        Add notifications from a list of contracts to the list of notifications.

        Parameters
        ----------
        notifications: list[Notification]
            A list of notifications to be added.

        Returns
        -------
        None

        Examples
        --------
        >>> obj = Notifiable()

        >>> obj.add_notifications_of_contract([Notification("key", "message")])

        """
        self._notifications += self._filter_and_map_notifiables(notifications)

    def _filter_and_map_notifiables(
        self, *notifications: list[Notification]
    ) -> list[Notification]:
        """
        Filter and maps notifications from notifiable objects.

        Parameters
        ----------
        notifications: list[Notification]
            A list of notifications to be filtered and mapped.

        Returns
        -------
        list[Notification]
            A list of notifications.

        Examples
        --------
        >>> obj = Notifiable()

        >>> obj._filter_and_map_notifiables([Notification("key", "message")])

        """
        return [
            notification
            for notifiable in notifications
            if isinstance(notifiable, Notifiable)
            for notification in notifiable._notifications
        ]

    def _filter_notifications(
        self, notifications: list[Notification]
    ) -> list[Notification]:
        """
        Filter notifications to ensure they are instances of Notification.

        Parameters
        ----------
        notifications: list[Notification]
            A list of notifications to be filtered.

        Returns
        -------
        list[Notification]
            A list of notifications.

        Examples
        --------
        >>> obj = Notifiable()

        >>> obj._filter_notifications([Notification("key","message")])

        """
        return [
            notification
            for notification in notifications
            if isinstance(notification, Notification)
        ]

    def get_notifications(self) -> list[Notification]:
        """
        Return the list of notifications.

        Returns
        -------
        list[Notification]
            A list of notifications.

        Examples
        --------
        >>> obj = Notifiable()

        >>> obj.get_notifications()

        """
        return self._notifications

    def clear(self):
        """
        Clear the list of notifications.

        Returns
        -------
        None

        Examples
        --------
        >>> obj = Notifiable()

        >>> obj.clear()

        """
        self._notifications.clear()

    def is_valid(self) -> bool:
        """
        Check if there are any notifications.

        Returns
        -------
        bool
            True if there are no notifications, False otherwise.

        Examples
        --------
        >>> obj = Notifiable()

        >>> obj.is_valid()

        """
        if len(self._notifications) <= 0:
            return True
        return False

    def __str__(self) -> str:
        """
        Return a string representation of the list of notifications.

        Returns
        -------
        str
            A string representation of the list of notifications.

        Examples
        --------
        >>> obj = Notifiable()

        >>> obj.__str__()

        """
        return self._notifications.__str__()
