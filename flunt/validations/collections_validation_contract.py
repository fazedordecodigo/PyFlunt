"""Module Contract."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self

from flunt.constants.messages import (
    GREATER_OR_EQUALS_THAN,
    GREATER_THAN,
    IS_BETWEEN,
    IS_NOT_SIZED,
    LOWER_OR_EQUALS_THAN,
    LOWER_THAN,
)
from flunt.notifications.notifiable import Notifiable

if TYPE_CHECKING:
    from collections.abc import Sized


class CollectionsValidationContract(Notifiable):
    """
    Class for validating values and adding notifications based on various comparisons.

    This class provides methods for validating collection lengths and adding
    notifications based on various comparison criteria.

    Attributes:
        None

    """

    def is_lower_than(
        self,
        value: Sized,
        comparer: int,
        field: str,
        message: str = LOWER_THAN,
    ) -> Self:
        """
        Check if the length of a collection value is lower than a given number and adds a notification if it's greater.

        Args:
            value (Sized): The collection value to compare (str, list, dict, set, tuple, range, bytearray).
            comparer (int): The maximum length allowed for the value.
            field (str): The field or identifier associated with the comparison.
            message (str, optional): The notification message to be added if the length exceeds the comparer.
                Defaults to LOWER_THAN.

        Returns:
            Self: The current instance with potential notifications added.

        Note:
            - If the `value` is an empty string or None, no notification is added.
            - If the length of `value` is greater than `comparer`, a notification is added to the current instance
              with the provided `field` and `message`.

        Example:
            ```python
            obj = Contract()
                    .is_lower_than("Hello", 10, "LengthCheck", "Value should have a length less than 10")
            obj.is_valid
            ```

        """
        if not value:
            return self

        if not hasattr(value, "__iter__"):
            self.add_notification(field, IS_NOT_SIZED)
            return self

        if len(value) >= comparer:
            if message is LOWER_THAN:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self

    def is_lower_or_equals_than(
        self,
        value: Sized,
        comparer: int,
        field: str,
        message: str = LOWER_OR_EQUALS_THAN,
    ) -> Self:
        """
        Check if the length of a collection value is lower or equal to a given number and adds a notification if it exceeds.

        Args:
            value (Sized): The collection value to compare (str, list, dict, set, tuple, range, bytearray).
            comparer (int): The maximum length allowed for the value.
            field (str): The field or identifier associated with the comparison.
            message (str, optional): The notification message to be added if the length exceeds the comparer.
                Defaults to LOWER_OR_EQUALS_THAN.

        Returns:
            Self: The current instance with potential notifications added.

        Note:
            - If the `value` is an empty string or None, no notification is added.
            - If the length of `value` is greater than or equal to `comparer`, a notification is added to the current instance
              with the provided `field` and `message`.

        Example:
            ```python
            obj = Contract()
                    .is_lower_or_equals_than("Hello", 10, "LengthCheck", "Value should have a length less than or equal to 10")
            obj.is_valid
            ```

        """
        if not value:
            return self

        if not hasattr(value, "__iter__"):
            self.add_notification(field, IS_NOT_SIZED)
            return self

        if len(value) > comparer:
            if message is LOWER_OR_EQUALS_THAN:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self

    def is_greater_than(
        self,
        value: Sized,
        comparer: int,
        field: str,
        message: str = GREATER_THAN,
    ) -> Self:
        """
        Check if the length of a collection value is greater than a given number and adds a notification if it's smaller.

        Args:
            value (Sized): The collection value to compare (str, list, dict, set, tuple, range, bytearray).
            comparer (int): The minimum length required for the value.
            field (str): The field or identifier associated with the comparison.
            message (str, optional): The notification message to be added if the length is smaller than the comparer.
                Defaults to GREATER_THAN.

        Returns:
            Self: The current instance with potential notifications added.

        Note:
            - If the `value` is an empty string or None, no notification is added.
            - If the length of `value` is smaller than `comparer`, a notification is added to the current instance
              with the provided `field` and `message`.

        Example:
            ```python
            obj = Contract()
                .is_greater_than("Hello", 3, "LengthCheck", "Value should have a length greater than 3")
            obj.is_valid
            ```

        """
        if not value:
            return self

        if not hasattr(value, "__iter__"):
            self.add_notification(field, IS_NOT_SIZED)
            return self

        if len(value) <= comparer:
            if message is GREATER_THAN:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self

    def is_greater_or_equals_than(
        self,
        value: Sized,
        comparer: int,
        field: str,
        message: str = GREATER_OR_EQUALS_THAN,
    ) -> Self:
        """
        Check if the length of a collection value is greater than or equal to a given number and adds a notification if it's smaller.

        Args:
            value (Sized): The collection value to compare (str, list, dict, set, tuple, range, bytearray).
            comparer (int): The minimum length required for the value.
            field (str): The field or identifier associated with the comparison.
            message (str, optional): The notification message to be added if the length is smaller than the comparer.
                Defaults to GREATER_OR_EQUALS_THAN.

        Returns:
            Self: The current instance with potential notifications added.

        Note:
            - If the `value` is an empty string or None, no notification is added.
            - If the length of `value` is smaller than or equal to `comparer`, a notification is added to the current instance
              with the provided `field` and `message`.

        Example:
            ```python
            obj = Contract()
                .is_greater_or_equals_than("Hello", 3, "LengthCheck", "Value should have a length greater than or equal to 3")
            obj.is_valid
            ```

        """
        if not value:
            return self

        if not hasattr(value, "__iter__"):
            self.add_notification(field, IS_NOT_SIZED)
            return self

        if len(value) < comparer:
            if message is GREATER_OR_EQUALS_THAN:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self

    def is_between(
        self,
        value: Sized,
        min: int,
        max: int,
        field: str,
        message: str = IS_BETWEEN,
    ) -> Self:
        """
        Require a collection value to have a length between a minimum and maximum value (inclusive).

        Args:
            value (Sized): The collection value to be checked (str, list, dict, set, tuple, range, bytearray).
            min (int): The minimum allowed length for the value.
            max (int): The maximum allowed length for the value.
            field (str): The field or identifier associated with the length check.
            message (str, optional): The notification message to be added if the length is outside the range.
                Defaults to IS_BETWEEN.

        Returns:
            Self: The current instance with potential notifications added.

        Note:
            - If the `value` is empty, the function returns the current instance without adding any notifications.
            - If the `value` is None or consists only of whitespace characters, the function returns the current instance without adding any notifications.
            - If the length of `value` is less than `min` or greater than `max`, a notification is added to the current instance
              with the provided `field` and `message`.

        Example:
            ```python
            obj = Contract().is_between(
                "Hello",
                3,
                6,
                "LengthCheck",
                "Value length should be between 3 and 6",
            )
            obj.is_valid
            ```

        """
        if not value:
            return self

        if not hasattr(value, "__iter__"):
            self.add_notification(field, IS_NOT_SIZED)
            return self

        if not min <= len(value) <= max:
            if message is IS_BETWEEN:
                self.add_notification(field, message.format(field, min, max))
                return self
            self.add_notification(field, message)
        return self
