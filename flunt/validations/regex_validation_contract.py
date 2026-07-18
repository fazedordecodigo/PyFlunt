"""Module Regex Validation Contract."""

from __future__ import annotations

import re
from typing import Self

from flunt.constants.messages import MATCHES, NOT_MATCHES
from flunt.notifications.notifiable import Notifiable


class RegexValidationContract(Notifiable):
    """Contract for validating strings against regex patterns.

    Methods:
        matches: Requires a string matches a regex pattern.
        not_matches: Requires a string does not match a regex pattern.

    """

    def matches(
        self, val: str, pattern: str, field: str, message: str = MATCHES
    ) -> Self:
        """Require a string matches a regex pattern.

        Args:
            val: The string value to test.
            pattern: The regex pattern to match against.
            field: The field or identifier associated with the check.
            message: The notification message if the value does not match.

        Returns:
            The current instance with potential notifications added.

        """
        if not re.match(pattern, val or ""):
            if message == MATCHES:
                self.add_notification(field, message.format(field, pattern))
                return self
            self.add_notification(field, message)
        return self

    def not_matches(
        self, val: str, pattern: str, field: str, message: str = NOT_MATCHES
    ) -> Self:
        """Require a string does not match a regex pattern.

        Args:
            val: The string value to test.
            pattern: The regex pattern to test against.
            field: The field or identifier associated with the check.
            message: The notification message if the value matches.

        Returns:
            The current instance with potential notifications added.

        """
        if re.match(pattern, val or ""):
            if message == NOT_MATCHES:
                self.add_notification(field, message.format(field, pattern))
                return self
            self.add_notification(field, message)
        return self
