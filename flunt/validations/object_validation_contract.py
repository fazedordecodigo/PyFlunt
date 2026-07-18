"""Module Object Validation Contract."""

from __future__ import annotations

from typing import Self

from flunt.constants.messages import EQUALS, IS_NONE, NOT_EQUALS, REQUIRED
from flunt.notifications.notifiable import Notifiable


class ObjectValidationContract(Notifiable):
    """Contract for validating objects.

    Methods:
        is_null: Requires an object is None.
        is_not_null: Requires an object is not None.
        are_equals: Requires two objects are equal.
        are_not_equals: Requires two objects are not equal.

    """

    def is_null(self, val: object, field: str, message: str = IS_NONE) -> Self:
        """Require an object is None.

        Args:
            val: The value to be checked.
            field: The field or identifier associated with the check.
            message: The notification message if the value is not None.

        Returns:
            The current instance with potential notifications added.

        """
        if val is not None:
            if message == IS_NONE:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self

    def is_not_null(
        self, val: object, field: str, message: str = REQUIRED
    ) -> Self:
        """Require an object is not None.

        Args:
            val: The value to be checked.
            field: The field or identifier associated with the check.
            message: The notification message if the value is None.

        Returns:
            The current instance with potential notifications added.

        """
        if val is None:
            if message == REQUIRED:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self

    def are_equals(
        self, val: object, comparer: object, field: str, message: str = EQUALS
    ) -> Self:
        """Require two objects are equal.

        Args:
            val: The first value to compare.
            comparer: The second value to compare.
            field: The field or identifier associated with the comparison.
            message: The notification message if values are not equal.

        Returns:
            The current instance with potential notifications added.

        """
        if val is None or comparer is None:
            return self
        if val != comparer:
            if message == EQUALS:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self

    def are_not_equals(
        self, val: object, comparer: object, field: str, message: str = NOT_EQUALS
    ) -> Self:
        """Require two objects are not equal.

        Args:
            val: The first value to compare.
            comparer: The second value to compare.
            field: The field or identifier associated with the comparison.
            message: The notification message if values are equal.

        Returns:
            The current instance with potential notifications added.

        """
        if val is None or comparer is None:
            return self
        if val == comparer:
            if message == NOT_EQUALS:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self
