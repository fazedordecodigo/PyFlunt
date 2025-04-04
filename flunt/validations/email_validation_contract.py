"""Module Email Validation Contract."""

from __future__ import annotations

import re
from functools import lru_cache
from re import Pattern
from typing import Self, TypeAlias

from flunt.constants.messages import IS_EMAIL, IS_NOT_EMAIL
from flunt.localization.flunt_regex_patterns import get_pattern
from flunt.notifications.notifiable import Notifiable

EmailType: TypeAlias = str | None


@lru_cache(maxsize=1)
def _get_email_pattern() -> Pattern[str] | None:
    """
    Get the email validation pattern with caching.

    Returns:
        The regex pattern for email validation or None if not available

    """
    pattern = get_pattern("email")
    if pattern is None:
        return None
    return re.compile(pattern, re.IGNORECASE)


def _valid_email(value: EmailType) -> bool:
    """
    Check if a string matches a valid email pattern.

    Args:
        value: The string to check as an email address

    Returns:
        True if valid email, False otherwise

    Example:
        >>> _valid_email("user@example.com")
        True
        >>> _valid_email("invalid-email")
        False
        >>> _valid_email(None)
        False

    """
    if not isinstance(value, str):
        return False

    pattern = _get_email_pattern()
    if pattern is None:
        return False

    return bool(pattern.match(value))


class EmailValidationContract(Notifiable):
    """
    Contract for validating email addresses.

    This class provides methods for validating email addresses and adding notifications
    based on validation results.

    Attributes:
        __slots__: Define os atributos permitidos para otimização de memória

    """

    def is_email(
        self, value: EmailType, field: str, message: str = IS_EMAIL
    ) -> Self:
        """
        Check if a string is a valid email address.

        Args:
            value: The string to check as an email address
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Example:
            >>> contract = EmailValidationContract()
            >>> contract.is_email("invalid-email", "email")
            >>> contract.is_valid  # False
            >>> contract.is_email("user@example.com", "email")
            >>> contract.is_valid  # True
            >>> contract.is_email(None, "email")
            >>> contract.is_valid  # False

        """
        if not _valid_email(value):
            if message is IS_EMAIL:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self

    def is_not_email(
        self, value: EmailType, field: str, message: str = IS_NOT_EMAIL
    ) -> Self:
        """
        Check if a string is not a valid email address.

        Args:
            value: The string to check as an email address
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Example:
            >>> contract = EmailValidationContract()
            >>> contract.is_not_email("user@example.com", "email")
            >>> contract.is_valid  # False
            >>> contract.is_not_email("invalid-email", "email")
            >>> contract.is_valid  # True
            >>> contract.is_not_email(None, "email")
            >>> contract.is_valid  # True

        """
        if _valid_email(value):
            if message is IS_NOT_EMAIL:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self
