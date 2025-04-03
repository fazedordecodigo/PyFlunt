"""Module Contract."""

from __future__ import annotations

from typing import Self, TypeAlias

from flunt.constants.messages import IS_FALSE, IS_TRUE
from flunt.notifications.notifiable import Notifiable

BoolType: TypeAlias = bool | int | str

def _to_bool(value: BoolType) -> bool:
    """
    Convert a value to boolean.

    Args:
        value: The value to convert

    Returns:
        The boolean representation of the value

    Example:
        >>> _to_bool(True)
        True
        >>> _to_bool(1)
        True
        >>> _to_bool("true")
        True
        >>> _to_bool(False)
        False
        >>> _to_bool(0)
        False
        >>> _to_bool("false")
        False

    """
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return bool(value)
    if isinstance(value, str):
        return value.lower() in ("true", "1", "yes", "on")
    return False

class BoolValidationContract(Notifiable):
    """
    Contract for validating boolean values.

    This class provides methods for validating boolean values and adding notifications
    based on validation results.

    Attributes:
        __slots__: Defines allowed attributes for memory optimization

    """

    def is_false(
        self, value: BoolType, field: str, message: str = IS_FALSE
    ) -> Self:
        """
        Check if a value is False.

        Args:
            value: The value to check (can be bool, int, or str)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Example:
            >>> contract = BoolValidationContract()
            >>> contract.is_false(True, "active")
            >>> contract.is_valid  # False
            >>> contract.is_false(False, "active")
            >>> contract.is_valid  # True
            >>> contract.is_false(1, "active")
            >>> contract.is_valid  # False
            >>> contract.is_false("true", "active")
            >>> contract.is_valid  # False

        """
        if message is IS_FALSE:
            message = IS_FALSE.format(field)

        if _to_bool(value):
            self.add_notification(field, message)
        return self

    def is_true(
        self, value: BoolType, field: str, message: str = IS_TRUE
    ) -> Self:
        """
        Check if a value is True.

        Args:
            value: The value to check (can be bool, int, or str)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Example:
            >>> contract = BoolValidationContract()
            >>> contract.is_true(False, "active")
            >>> contract.is_valid  # False
            >>> contract.is_true(True, "active")
            >>> contract.is_valid  # True
            >>> contract.is_true(0, "active")
            >>> contract.is_valid  # False
            >>> contract.is_true("false", "active")
            >>> contract.is_valid  # False

        """
        if message is IS_TRUE:
            message = IS_TRUE.format(field)
        if not _to_bool(value):
            self.add_notification(field, message)
        return self
