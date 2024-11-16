"""Module Notification."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Notification:
    """Class Notification."""

    field: str
    message: str
