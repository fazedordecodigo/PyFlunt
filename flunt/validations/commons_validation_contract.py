"""Module Contract."""

from __future__ import annotations

from typing import Self, TypeVar

from flunt.constants.messages import EQUALS, IS_NONE, NOT_EQUALS, REQUIRED
from flunt.notifications.notifiable import Notifiable

# Tipo genérico para qualquer valor
T = TypeVar("T")


class CommonsValidationContract(Notifiable):
    """
    Class for validating values and adding notifications based on various comparisons.

    Methods:
        is_none: Checks if a value is None.
        is_not_none: Checks if a value is not None.
        are_equals: Checks if two values are equal.
        are_not_equals: Checks if two values are not equal.

    """

    def is_none(self, value: T, field: str, message: str = IS_NONE) -> Self:
        """
        Check if value is not None and adds a notification if it is.

        Args:
            value: The value to be checked.
            field: The field or identifier associated with the check.
            message: The notification message to be added if the value is None.
                    If not provided, a default message will be used.

        Returns:
            The current instance with potential notifications added.

        Examples:
            ```python
            obj = Contract().is_none(
                "Hello", "ValueCheck", "Value should not be None"
            )
            obj.is_valid
            ```

        """
        if value is not None:
            if message is IS_NONE:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self

    def is_not_none(
        self, value: T, field: str, message: str = REQUIRED
    ) -> Self:
        """
        Check if a value is not None and adds a notification if it is.

        Args:
            value: The value to be checked.
            field: The field or identifier associated with the check.
            message: The notification message to be added if the value is None.
                    If not provided, a default message will be used.

        Returns:
            The current instance with potential notifications added.

        Examples:
            ```python
            obj = Contract().is_not_none(
                None, "ValueCheck", "Value should not be None"
            )
            obj.is_valid
            ```

        """
        if value is None:
            if message is REQUIRED:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self

    def are_equals(
        self, value: T, comparer: T, field: str, message: str = EQUALS
    ) -> Self:
        """
        Check if two values are equal and adds a notification if they are not equal.

        Args:
            value: The first value to compare.
            comparer: The second value to compare with the first value.
            field: The field or identifier associated with the comparison.
            message: The notification message to be added if the values are not equal.
                    If not provided, a default message will be used.

        Returns:
            The current instance with potential notifications added.

        Examples:
            ```python
            obj = Contract().are_equals(
                "Hello",
                "Hello",
                "Comparison",
                "Values should be equal",
            )
            obj.is_valid
            ```

        """
        if value != comparer:
            if message is EQUALS:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self

    def are_not_equals(
        self, value: T, comparer: T, field: str, message: str = NOT_EQUALS
    ) -> Self:
        """
        Require two values are not equals.

        Args:
            value: The value to be compared.
            comparer: The value to compare with `value`.
            field: The field or identifier related to the comparison.
            message: The notification message in case of equal values.
                    If not provided, a default message will be used.

        Returns:
            The current instance with potential notifications added.

        Examples:
            ```python
            obj = Contract().are_not_equals(
                "Hello",
                "World",
                "Comparison",
                "Values should not be equal",
            )
            obj.is_valid
            ```

        """
        if value == comparer:
            if message is NOT_EQUALS:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self
