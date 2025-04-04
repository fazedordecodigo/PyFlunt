"""Module Contract."""

from __future__ import annotations

import re
from functools import lru_cache
from re import Pattern
from typing import Self, TypeAlias

from flunt.constants.messages import IS_NOT_CREDIT_CARD
from flunt.localization.flunt_regex_patterns import get_pattern
from flunt.notifications.notifiable import Notifiable

CreditCardType: TypeAlias = str | None


@lru_cache(maxsize=1)
def _get_only_numbers_pattern() -> Pattern[str] | None:
    """
    Get the only numbers validation pattern with caching.

    Returns:
        The regex pattern for only numbers validation or None if not available

    """
    pattern = get_pattern("only_numbers")
    if pattern is None:
        return None
    return re.compile(pattern, re.IGNORECASE)


def _luhn_checksum(value: str) -> bool:
    """
    Validate a credit card number using the Luhn algorithm.

    Args:
        value: The credit card number to validate

    Returns:
        True if valid, False otherwise

    Example:
        >>> _luhn_checksum("4532015112830366")
        True
        >>> _luhn_checksum("4532015112830367")
        False

    """
    if not value.isdigit():
        return False

    even = False
    checksum = 0

    for digit in reversed(value):
        val = int(digit) * (2 if even else 1)
        even = not even

        while val > 0:
            checksum += val % 10
            val //= 10

    return checksum % 10 == 0


class CreditCardValidationContract(Notifiable):
    """
    Contract for validating credit card numbers.

    This class provides methods for validating credit card numbers and adding notifications
    based on validation results.

    Attributes:
        __slots__: Define os atributos permitidos para otimização de memória

    """

    def is_credit_card(
        self,
        value: CreditCardType,
        field: str,
        message: str = IS_NOT_CREDIT_CARD,
    ) -> Self:
        """
        Check if a string is a valid credit card number using Luhn algorithm.

        Args:
            value: The string to check as a credit card number
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Example:
            >>> contract = CreditCardValidationContract()
            >>> contract.is_credit_card("4532015112830366", "card")
            >>> contract.is_valid  # True
            >>> contract.is_credit_card("4532015112830367", "card")
            >>> contract.is_valid  # False
            >>> contract.is_credit_card("invalid", "card")
            >>> contract.is_valid  # False
            >>> contract.is_credit_card(None, "card")
            >>> contract.is_valid  # False

        """
        if not isinstance(value, str):
            self.add_notification(field, message.format(field))
            return self

        pattern = _get_only_numbers_pattern()
        if pattern is None or not pattern.match(value):
            if message is IS_NOT_CREDIT_CARD:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
            return self

        if not _luhn_checksum(value):
            if message is IS_NOT_CREDIT_CARD:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self
