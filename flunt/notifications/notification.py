"""Module Notification."""

from dataclasses import dataclass


@dataclass
class Notification:
    """Class Notification."""

    field: str
    message: str
