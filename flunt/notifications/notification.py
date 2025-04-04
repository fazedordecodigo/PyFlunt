"""Module Notification."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Notification:
    """Class Notification."""

    field: str
    message: str

    def __str__(self) -> str:
        """Return the string representation of the notification."""
        return f"{self.field}: {self.message}"

    def __repr__(self) -> str:
        """Return the string representation of the notification."""
        return f"{self.field}: {self.message}"
