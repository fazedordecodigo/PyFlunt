"""Module Contract."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self

from flunt.constants.messages import (
    GREATER_OR_EQUALS_THAN,
    GREATER_THAN,
    IS_BETWEEN,
    LOWER_OR_EQUALS_THAN,
    LOWER_THAN,
)
from flunt.notifications.notifiable import Notifiable

if TYPE_CHECKING:
    from collections.abc import Sized


class CollectionsValidationContract(Notifiable):
    """
    Class for validating values and adding notifications based on various comparisons.

    Parameters
    ----------
            N/A

    Attributes
    ----------
            N/A

    Methods
    -------
    - is_lower_than(value, comparer, field, message): Checks if the length of a collection value is lower than a given number.
    - is_lower_or_equals_than(value, comparer, field, message): Checks if the length of a collection value is lower or equal to a given number.
    - is_greater_than(value, comparer, field, message): Checks if the length of a collection value is greater than a given number.
    - is_greater_or_equals_than(value, comparer, field, message): Checks if the length of a collection value is greater or equal to a given number.
    - is_between(value, min, max, field, message): Checks if the length of a collection is between a minimum and maximum value.

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

        Parameters
        ----------
        `value`: str | list | dict | set | tuple | range | bytearray
            The collection value to compare.
        `comparer`: int
            The maximum length allowed for the value.
        `field`: str
            The field or identifier associated with the comparison.
        `message`: str
            The notification message to be added if the length exceeds the comparer.

        Returns
        -------
        `self`
             The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is an empty string or None, no notification is added.
        - If the length of `value` is greater than `comparer`, a notification is added to the current instance
        with the provided `field` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
                .is_lower_than("Hello", 10, "LengthCheck", "Value should have a length less than 10")
        obj.is_valid
        ```

        """
        if not value:
            return self

        if not hasattr(value, "__iter__"):
            self.add_notification(field, "Value is not Sized")
            return self

        if message is LOWER_THAN:
            message = LOWER_THAN.format(field, comparer)

        if len(value) >= comparer:
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

        Parameters
        ----------
        `value`: str | list | dict | set | tuple | range | bytearray
            The collection value to compare.
        `comparer`: int
            The maximum length allowed for the value.
        `field`: str
            The field or identifier associated with the comparison.
        `message`: str
            The notification message to be added if the length exceeds the comparer.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is an empty string or None, no notification is added.
        - If the length of `value` is greater than or equal to `comparer`, a notification is added to the current instance
        with the provided `field` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
                .is_lower_or_equals_than("Hello", 10, "LengthCheck", "Value should have a length less than or equal to 10")
        obj.is_valid
        ```

        """
        if not value:
            return self

        if not hasattr(value, "__iter__"):
            self.add_notification(field, "Value is not Sized")
            return self

        if message is LOWER_OR_EQUALS_THAN:
            message = LOWER_OR_EQUALS_THAN.format(field, comparer)

        if len(value) > comparer:
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

        Parameters
        ----------
        `value`: str | list | dict | set | tuple | range | bytearray
            The collection value to compare.
        `comparer`: int
            The minimum length required for the value.
        `field`: str
            The field or identifier associated with the comparison.
        `message`: str
            The notification message to be added if the length is smaller than the comparer.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is an empty string or None, no notification is added.
        - If the length of `value` is smaller than `comparer`, a notification is added to the current instance
        with the provided `field` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
            .is_greater_than("Hello", 3, "LengthCheck", "Value should have a length greater than 3")
        obj.is_valid
        ```

        """
        if not value:
            return self

        if not hasattr(value, "__iter__"):
            self.add_notification(field, "Value is not Sized")
            return self

        if message is GREATER_THAN:
            message = GREATER_THAN.format(field, comparer)

        if len(value) <= comparer:
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

        Parameters
        ----------
        `value`: str | list | dict | set | tuple | range | bytearray
            The collection value to compare.
        `comparer`: int
            The minimum length required for the value.
        `field`: str
            The field or identifier associated with the comparison.
        `message`: str
            The notification message to be added if the length is smaller than the comparer.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is an empty string or None, no notification is added.
        - If the length of `value` is smaller than or equal to `comparer`, a notification is added to the current instance
        with the provided `field` and `message`.

        Example:
        --------
        ```python
        obj = Contract()
            .is_greater_or_equals_than("Hello", 3, "LengthCheck", "Value should have a length greater than or equal to 3")
        obj.is_valid
        ```

        """
        if not value:
            return self

        if not hasattr(value, "__iter__"):
            self.add_notification(field, "Value is not Sized")
            return self

        if message is GREATER_OR_EQUALS_THAN:
            message = GREATER_OR_EQUALS_THAN.format(field, comparer)

        if len(value) < comparer:
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
        Require a collection value to have a length between a minimum and maximum value (inclusive), and adds a notification if the length is outside the specified range.

        Parameters
        ----------
        `value`: str | list | dict | set | tuple | range | bytearray
            The collection value to be checked.
        `min`: int
            The minimum allowed length for the value.
        `max`: int
            The maximum allowed length for the value.
        `field`: str
            The field or identifier associated with the length check.
        `message`: str
            The notification message to be added if the length is outside the range.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is empty, the function returns the current instance without adding any notifications.
        - If the `value` is None or consists only of whitespace characters, the function returns the current instance without adding any notifications.
        - If the length of `value` is less than `min` or greater than `max`, a notification is added to the current instance
        with the provided `field` and `message`.

        Examples
        --------
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
            self.add_notification(field, "Value is a not collection")
            return self

        if message is IS_BETWEEN:
            message = IS_BETWEEN.format(field, min, max)

        if not min <= len(value) <= max:
            self.add_notification(field, message)
        return self
