"""Module Contract."""

from __future__ import annotations

from typing import Self, TypeVar

from flunt.constants.messages import REQUIRED
from flunt.notifications.notifiable import Notifiable
from flunt.validations.bool_validation_contract import (
    BoolValidationContract,
)
from flunt.validations.collections_validation_contract import (
    CollectionsValidationContract,
)
from flunt.validations.commons_validation_contract import (
    CommonsValidationContract,
)
from flunt.validations.credit_card_validation_contract import (
    CreditCardValidationContract,
)
from flunt.validations.email_validation_contract import (
    EmailValidationContract,
)
from flunt.validations.strings_validation_contract import (
    StringValidationContract,
)

# Tipo genérico para qualquer valor
T = TypeVar("T")


class Contract(
    BoolValidationContract,
    CollectionsValidationContract,
    CommonsValidationContract,
    CreditCardValidationContract,
    EmailValidationContract,
    StringValidationContract,
    Notifiable,
):
    """
    Contract for validating data.

    This class provides a comprehensive set of validation methods through
    multiple inheritance from specialized validation mixins.
    """

    def __init__(self) -> None:
        """Initialize the contract with all validation components."""
        super().__init__()

    def requires(
        self,
        value: T,
        field: str,
        message: str = REQUIRED,
    ) -> Self:
        """
        Check if a value is empty and add a notification if it is.

        Args:
            value: The value to check
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = Contract()
            >>> contract.requires("", "name")
            >>> contract.is_valid  # False
            >>> contract.requires(0, "age", "Age must be greater than 0")
            >>> contract.is_valid  # False

        """
        if not value and not isinstance(value, bool | int | float):
            if message is REQUIRED:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self
