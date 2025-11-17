"""Module DateTime Validation Contract."""

from __future__ import annotations

from datetime import date, datetime
from typing import Self

from flunt.notifications.notifiable import Notifiable


class DateTimeValidationContract(Notifiable):
    """
    Contract for validating date and datetime values.

    This class provides methods for validating dates and datetimes with
    common business rules.

    """

    def is_date_after(
        self,
        value: date | datetime | None,
        comparer: date | datetime,
        field: str,
        message: str = "The field {0} must be after {1}",
    ) -> Self:
        """
        Check if a date is after another date.

        Args:
            value: The date to check
            comparer: The date to compare against
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> from datetime import date
            >>> contract = DateTimeValidationContract()
            >>> contract.is_date_after(date(2024, 1, 15), date(2024, 1, 1), "data")
            >>> contract.is_valid  # True
            >>> contract.is_date_after(date(2023, 12, 1), date(2024, 1, 1), "data")
            >>> contract.is_valid  # False

        """
        if value is None or value <= comparer:
            self.add_notification(field, message.format(field, comparer))
        return self

    def is_date_before(
        self,
        value: date | datetime | None,
        comparer: date | datetime,
        field: str,
        message: str = "The field {0} must be before {1}",
    ) -> Self:
        """
        Check if a date is before another date.

        Args:
            value: The date to check
            comparer: The date to compare against
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> from datetime import date
            >>> contract = DateTimeValidationContract()
            >>> contract.is_date_before(date(2023, 12, 1), date(2024, 1, 1), "data")
            >>> contract.is_valid  # True
            >>> contract.is_date_before(date(2024, 1, 15), date(2024, 1, 1), "data")
            >>> contract.is_valid  # False

        """
        if value is None or value >= comparer:
            self.add_notification(field, message.format(field, comparer))
        return self

    def is_date_between(
        self,
        value: date | datetime | None,
        start: date | datetime,
        end: date | datetime,
        field: str,
        message: str = "The field {0} must be between {1} and {2}",
    ) -> Self:
        """
        Check if a date is between two dates (inclusive).

        Args:
            value: The date to check
            start: The start date (inclusive)
            end: The end date (inclusive)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> from datetime import date
            >>> contract = DateTimeValidationContract()
            >>> contract.is_date_between(
            ...     date(2024, 1, 15),
            ...     date(2024, 1, 1),
            ...     date(2024, 1, 31),
            ...     "data"
            ... )
            >>> contract.is_valid  # True

        """
        if value is None or not (start <= value <= end):
            self.add_notification(field, message.format(field, start, end))
        return self

    def is_date_in_past(
        self,
        value: date | datetime | None,
        field: str,
        message: str = "The field {0} must be in the past",
    ) -> Self:
        """
        Check if a date is in the past (before today).

        Args:
            value: The date to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> from datetime import date, timedelta
            >>> contract = DateTimeValidationContract()
            >>> past_date = date.today() - timedelta(days=1)
            >>> contract.is_date_in_past(past_date, "data_nascimento")
            >>> contract.is_valid  # True

        """
        today = datetime.now().date() if isinstance(value, datetime) else date.today()

        if value is None:
            self.add_notification(field, message.format(field))
            return self

        # Convert datetime to date for comparison
        value_date = value.date() if isinstance(value, datetime) else value

        if value_date >= today:
            self.add_notification(field, message.format(field))

        return self

    def is_date_in_future(
        self,
        value: date | datetime | None,
        field: str,
        message: str = "The field {0} must be in the future",
    ) -> Self:
        """
        Check if a date is in the future (after today).

        Args:
            value: The date to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> from datetime import date, timedelta
            >>> contract = DateTimeValidationContract()
            >>> future_date = date.today() + timedelta(days=1)
            >>> contract.is_date_in_future(future_date, "data_vencimento")
            >>> contract.is_valid  # True

        """
        today = datetime.now().date() if isinstance(value, datetime) else date.today()

        if value is None:
            self.add_notification(field, message.format(field))
            return self

        # Convert datetime to date for comparison
        value_date = value.date() if isinstance(value, datetime) else value

        if value_date <= today:
            self.add_notification(field, message.format(field))

        return self

    def is_today(
        self,
        value: date | datetime | None,
        field: str,
        message: str = "The field {0} must be today",
    ) -> Self:
        """
        Check if a date is today.

        Args:
            value: The date to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> from datetime import date
            >>> contract = DateTimeValidationContract()
            >>> contract.is_today(date.today(), "data_registro")
            >>> contract.is_valid  # True

        """
        today = datetime.now().date() if isinstance(value, datetime) else date.today()

        if value is None:
            self.add_notification(field, message.format(field))
            return self

        # Convert datetime to date for comparison
        value_date = value.date() if isinstance(value, datetime) else value

        if value_date != today:
            self.add_notification(field, message.format(field))

        return self
