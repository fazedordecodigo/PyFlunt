"""Module URL Validation Contract."""

from __future__ import annotations

from functools import lru_cache
from re import IGNORECASE, Pattern, compile
from typing import Self, TypeAlias

from flunt.constants.messages import IS_NOT_URL, IS_URL
from flunt.localization.flunt_regex_patterns import get_pattern
from flunt.notifications.notifiable import Notifiable

URLType: TypeAlias = str | None


@lru_cache(maxsize=1)
def _get_url_pattern() -> Pattern[str] | None:
    """
    Get the URL validation pattern with caching.

    Returns:
        The regex pattern for URL validation or None if not available

    """
    pattern = get_pattern("url")
    if pattern is None:
        return None
    return compile(pattern, IGNORECASE)


def _valid_url(value: URLType) -> bool:
    """
    Check if a string matches a valid URL pattern.

    Args:
        value: The string to check as a URL

    Returns:
        True if valid URL, False otherwise

    Examples:
        >>> _valid_url("https://example.com")
        True
        >>> _valid_url("http://localhost:8000")
        True
        >>> _valid_url("invalid-url")
        False
        >>> _valid_url(None)
        False

    """
    if not isinstance(value, str):
        return False

    pattern = _get_url_pattern()
    if pattern is None:
        return False

    return bool(pattern.match(value))


class URLValidationContract(Notifiable):
    """
    Contract for validating URLs.

    This class provides methods for validating URLs and adding notifications
    based on validation results.

    """

    def is_url(
        self, value: URLType, field: str, message: str = IS_URL
    ) -> Self:
        """
        Check if a string is a valid URL.

        Args:
            value: The string to check as a URL
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = URLValidationContract()
            >>> contract.is_url("https://example.com", "website")
            >>> contract.is_valid  # True
            >>> contract.is_url("not-a-url", "website")
            >>> contract.is_valid  # False
            >>> contract.is_url("http://localhost:3000", "api")
            >>> contract.is_valid  # True

        """
        if not _valid_url(value):
            if message is IS_URL:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self

    def is_not_url(
        self, value: URLType, field: str, message: str = IS_NOT_URL
    ) -> Self:
        """
        Check if a string is not a valid URL.

        Args:
            value: The string to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = URLValidationContract()
            >>> contract.is_not_url("just a text", "campo")
            >>> contract.is_valid  # True
            >>> contract.is_not_url("https://example.com", "campo")
            >>> contract.is_valid  # False

        """
        if _valid_url(value):
            if message is IS_NOT_URL:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self
