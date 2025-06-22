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
    Contract for validating string values.

    This class provides methods for common string validations and adds notifications
    based on validation results.

    Attributes:
        __slots__: Define os atributos permitidos para otimização de memória

    """

    def is_not_none_or_white_space(
        self,
        value: str | None,
        field: str,
        message: str = IS_NOT_NONE_OR_WHITESPACE,
    ) -> Self:
        """
        Check if a string value is not None or whitespace.

        Args:
            value: The string value to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Example:
            >>> contract = StringValidationContract()
            >>> contract.is_not_none_or_white_space("", "name")
            >>> contract.is_valid  # False
            >>> contract.is_not_none_or_white_space(None, "email")
            >>> contract.is_valid  # False
            >>> contract.is_not_none_or_white_space("John", "name")
            >>> contract.is_valid  # True

        """
        if value is None or not str(value).strip():
            if message is IS_NOT_NONE_OR_WHITESPACE:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self

    def contains(
        self,
        value: str | None,
        comparer: str,
        field: str,
        message: str = CONTAINS,
    ) -> Self:
        """
        Check if a string contains another string.

        Args:
            value: The string to search in
            comparer: The string to search for
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Example:
            >>> contract = StringValidationContract()
            >>> contract.contains("hello world", "world", "text")
            >>> contract.is_valid  # True
            >>> contract.contains("hello", "world", "text")
            >>> contract.is_valid  # False

        """
        if not isinstance(value, str) or comparer not in value:
            if message is CONTAINS:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self

    def not_contains(
        self,
        value: str | None,
        comparer: str,
        field: str,
        message: str = NOT_CONTAINS,
    ) -> Self:
        """
        Check if a string does not contain another string.

        Args:
            value: The string to search in
            comparer: The string to search for
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Example:
            >>> contract = StringValidationContract()
            >>> contract.not_contains("hello world", "world", "text")
            >>> contract.is_valid  # False
            >>> contract.not_contains("hello", "world", "text")
            >>> contract.is_valid  # True

        """
        if not isinstance(value, str) or comparer in value:
            if message is NOT_CONTAINS:
                self.add_notification(field, message.format(field, comparer))
                return self
            self.add_notification(field, message)
        return self
