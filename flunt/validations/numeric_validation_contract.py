"""Module Numeric Validation Contract."""

from __future__ import annotations

from typing import Self

from flunt.notifications.notifiable import Notifiable


class NumericValidationContract(Notifiable):
    """
    Contract for validating numeric values (int, float).

    This class provides methods for validating numbers directly, not collection sizes.
    For collection size validation, use CollectionsValidationContract.

    """

    def is_greater_than_number(
        self,
        value: float | None,
        comparer: float,
        field: str,
        message: str = "The field {0} must be greater than {1}",
    ) -> Self:
        """
        Check if a numeric value is greater than a given number.

        Args:
            value: The numeric value to check
            comparer: The minimum value (exclusive)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = NumericValidationContract()
            >>> contract.is_greater_than_number(25, 18, "idade")
            >>> contract.is_valid  # True
            >>> contract.is_greater_than_number(15, 18, "idade")
            >>> contract.is_valid  # False

        """
        if value is None or value <= comparer:
            self.add_notification(field, message.format(field, comparer))
        return self

    def is_greater_or_equals_than_number(
        self,
        value: float | None,
        comparer: float,
        field: str,
        message: str = "The field {0} must be greater than or equal to {1}",
    ) -> Self:
        """
        Check if a numeric value is greater than or equal to a given number.

        Args:
            value: The numeric value to check
            comparer: The minimum value (inclusive)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = NumericValidationContract()
            >>> contract.is_greater_or_equals_than_number(18, 18, "idade")
            >>> contract.is_valid  # True
            >>> contract.is_greater_or_equals_than_number(17, 18, "idade")
            >>> contract.is_valid  # False

        """
        if value is None or value < comparer:
            self.add_notification(field, message.format(field, comparer))
        return self

    def is_lower_than_number(
        self,
        value: float | None,
        comparer: float,
        field: str,
        message: str = "The field {0} must be lower than {1}",
    ) -> Self:
        """
        Check if a numeric value is lower than a given number.

        Args:
            value: The numeric value to check
            comparer: The maximum value (exclusive)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = NumericValidationContract()
            >>> contract.is_lower_than_number(15, 18, "idade")
            >>> contract.is_valid  # True
            >>> contract.is_lower_than_number(25, 18, "idade")
            >>> contract.is_valid  # False

        """
        if value is None or value >= comparer:
            self.add_notification(field, message.format(field, comparer))
        return self

    def is_lower_or_equals_than_number(
        self,
        value: float | None,
        comparer: float,
        field: str,
        message: str = "The field {0} must be lower than or equal to {1}",
    ) -> Self:
        """
        Check if a numeric value is lower than or equal to a given number.

        Args:
            value: The numeric value to check
            comparer: The maximum value (inclusive)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = NumericValidationContract()
            >>> contract.is_lower_or_equals_than_number(18, 18, "idade")
            >>> contract.is_valid  # True
            >>> contract.is_lower_or_equals_than_number(19, 18, "idade")
            >>> contract.is_valid  # False

        """
        if value is None or value > comparer:
            self.add_notification(field, message.format(field, comparer))
        return self

    def is_between_numbers(
        self,
        value: float | None,
        min_value: float,
        max_value: float,
        field: str,
        message: str = "The field {0} must be between {1} and {2}",
    ) -> Self:
        """
        Check if a numeric value is between two numbers (inclusive).

        Args:
            value: The numeric value to check
            min_value: The minimum value (inclusive)
            max_value: The maximum value (inclusive)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = NumericValidationContract()
            >>> contract.is_between_numbers(25, 18, 65, "idade")
            >>> contract.is_valid  # True
            >>> contract.is_between_numbers(70, 18, 65, "idade")
            >>> contract.is_valid  # False

        """
        if value is None or not (min_value <= value <= max_value):
            self.add_notification(
                field, message.format(field, min_value, max_value)
            )
        return self

    def is_positive(
        self,
        value: float | None,
        field: str,
        message: str = "The field {0} must be positive",
    ) -> Self:
        """
        Check if a numeric value is positive (greater than zero).

        Args:
            value: The numeric value to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = NumericValidationContract()
            >>> contract.is_positive(10, "quantidade")
            >>> contract.is_valid  # True
            >>> contract.is_positive(-5, "quantidade")
            >>> contract.is_valid  # False
            >>> contract.is_positive(0, "quantidade")
            >>> contract.is_valid  # False

        """
        if value is None or value <= 0:
            self.add_notification(field, message.format(field))
        return self

    def is_negative(
        self,
        value: float | None,
        field: str,
        message: str = "The field {0} must be negative",
    ) -> Self:
        """
        Check if a numeric value is negative (less than zero).

        Args:
            value: The numeric value to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = NumericValidationContract()
            >>> contract.is_negative(-10, "saldo")
            >>> contract.is_valid  # True
            >>> contract.is_negative(5, "saldo")
            >>> contract.is_valid  # False
            >>> contract.is_negative(0, "saldo")
            >>> contract.is_valid  # False

        """
        if value is None or value >= 0:
            self.add_notification(field, message.format(field))
        return self

    def is_zero(
        self,
        value: float | None,
        field: str,
        message: str = "The field {0} must be zero",
    ) -> Self:
        """
        Check if a numeric value is zero.

        Args:
            value: The numeric value to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = NumericValidationContract()
            >>> contract.is_zero(0, "contador")
            >>> contract.is_valid  # True
            >>> contract.is_zero(5, "contador")
            >>> contract.is_valid  # False

        """
        if value is None or value != 0:
            self.add_notification(field, message.format(field))
        return self

    def is_not_zero(
        self,
        value: float | None,
        field: str,
        message: str = "The field {0} must not be zero",
    ) -> Self:
        """
        Check if a numeric value is not zero.

        Args:
            value: The numeric value to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = NumericValidationContract()
            >>> contract.is_not_zero(5, "divisor")
            >>> contract.is_valid  # True
            >>> contract.is_not_zero(0, "divisor")
            >>> contract.is_valid  # False

        """
        if value is None or value == 0:
            self.add_notification(field, message.format(field))
        return self
