"""Module Contract."""
from __future__ import annotations

from typing import Self

from flunt.constants.messages import (
    CONTAINS,
    IS_NOT_NONE_OR_WHITESPACE,
    NOT_CONTAINS,
)
from flunt.notifications.notifiable import Notifiable


class StringValidationContract(Notifiable):
    """
    Class for validating string values and adding notifications based on various comparisons.

    Parameters
    ----------
            N/A

    Attributes
    ----------
            N/A

    Methods
    -------
    - is_not_none_or_white_space(value, field, message): Checks if a string value is not None or whitespace.
    - contains(value, comparer, field, message): Checks if a string value contains another string.
    - not_contains(value, comparer, field, message): Checks if a string value does not contain another string.

    """

    def is_not_none_or_white_space(
        self, value: str, field: str, message: str = IS_NOT_NONE_OR_WHITESPACE
    ) -> Self:
        """
        Check if a string value is not None or whitespace and adds a notification if it is.

        Parameters
        ----------
        `value`: str
                The string value to be checked.
        `field`: str
                The field or identifier associated with the check.
        `message`: str (optional)
                The notification message to be added if the value is None or whitespace.

        Returns
        -------
        `self`
                The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is None or consists only of whitespace characters (spaces, tabs, newlines, etc.),
        a notification is added to the current instance with the provided `field` and `message`.
        - If the `value` is not None and contains at least one non-whitespace character, no notification is added.

        Examples
        --------
        ```python
        obj = Contract()
                .is_not_none_or_white_space("Hello", "ValueCheck", "Value should not be None or whitespace")
        obj.is_valid
        ```

        """
        if value is None or value.isspace():
            self.add_notification(field, message.format(field))
        return self

    def contains(
        self, value: str, comparer: str, field: str, message: str = CONTAINS
    ) -> Self:
        """
        Check if a string value contains another string and adds a notification if it does.

        Parameters
        ----------
        `value`: str
                The string value to be checked.
        `comparer`: str
                The string to search for within the value.
        `field`: str
                The field or identifier associated with the check.
        `message`: str (optional)
                The notification message to be added if the value contains the comparer.

        Returns
        -------
        `self`
                The current instance with potential notifications added.

        Notes
        -----
        - If the `value` contains the `comparer` string, a notification is added to the current instance
        with the provided `field` and `message`.
        - If the `value` does not contain the `comparer` string, no notification is added.

        Examples
        --------
        ```python
        obj = Contract()
                .contains("Hello, world!", "world", "ContainsCheck", "Value should contain 'world'")
        obj.is_valid
        ```

        """
        if value.find(comparer) == -1:
            self.add_notification(field, message.format(field, comparer))
        return self

    def not_contains(
        self,
        value: str,
        comparer: str,
        field: str,
        message: str = NOT_CONTAINS,
    ) -> Self:
        """
        Check if a string value does not contain a specified string and adds a notification if it does.

        Parameters
        ----------
        `value`: str
                The string value to be checked.
        `comparer`: str
                The string to search for in the value.
        `field`: str
                The field or identifier associated with the check.
        `message`: str (optional)
                The notification message to be added if the value contains the comparer.

        Returns
        -------
        `self`
                The current instance with potential notifications added.

        Notes
        -----
        - If the `value` does not contain the `comparer` string, no notification is added.
        - If the `value` contains the `comparer` string, a notification is added to the current instance
        with the provided `field` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
                .not_contains("Hello", "World", "Comparison", "Value should not contain 'World'")
        obj.is_valid
        ```

        """
        if value.find(comparer) != -1:
            self.add_notification(field, message.format(field, comparer))
        return self
