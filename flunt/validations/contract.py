"""Module Contract."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, overload

from flunt.constants.messages import REQUIRED
from flunt.notifications.notifiable import Notifiable
from flunt.validations.bool_validation_contract import BoolValidationContract
from flunt.validations.collections_validation_contract import (
    CollectionsValidationContract,
)
from flunt.validations.commons_validation_contract import (
    CommonsValidationContract,
)
from flunt.validations.credit_card_validation_contract import (
    CreditCardValidationContract,
)
from flunt.validations.email_validation_contract import EmailValidationContract
from flunt.validations.strings_validation_contract import (
    StringValidationContract,
)

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable
    from decimal import Decimal
    from struct import Struct
    from uuid import UUID


class Contract(
    StringValidationContract,
    EmailValidationContract,
    BoolValidationContract,
    CreditCardValidationContract,
    CommonsValidationContract,
    CollectionsValidationContract,
    Notifiable,
):
    """
    Class represents a contract for validating data..

    Parameters
    ----------
            N/A

    Attributes
    ----------
            N/A

    Methods
    -------
    - requires(value, field: str, message: str): Checks if the given value is empty and adds a notification if it is.

    """

    @overload
    def requires(
        self, value: tuple, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: Struct, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: set, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: bool, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: dict, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: list, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: Iterable, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: Callable, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: str, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: Decimal, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: float, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: UUID, field: str, message: str = REQUIRED
    ) -> Self: ...

    @overload
    def requires(
        self, value: object, field: str, message: str = REQUIRED
    ) -> Self: ...

    def requires(
        self,
        value: str
        | float
        | list
        | bool
        | Decimal
        | UUID
        | dict
        | object
        | set
        | Struct
        | tuple
        | Iterable
        | Callable,
        field: str,
        message: str = REQUIRED,
    ) -> Self:
        """
        Check if the given value is empty and adds a notification if it is.

        Parameters
        ----------
        `value`: [bool | str | float | Tuple | Set | List | Iterable | Dict | Callable | Decimal | UUID | object | Struct]
                The value to be checked.
        `field`: str
                The field or identifier associated with the notification.
        `message`: str (optional)
                The message of the notification to be added.

        Returns
        -------
        `Self`
                The current instance of the class.

        Notes
        -----
        - If the provided `value` is empty, a `notification` is added to the current
        instance using the provided `field` and `message`.
        - If the provided `value` is not empty, no `notification` is added.

        Examples
        --------
        ```python
        contract = Contract().requires("", "field", "message")
        contract.is_valid  # False
        ```

        """
        if message is REQUIRED:
            message = REQUIRED.format(field)

        if not value and not isinstance(value, bool):
            self.add_notification(field, message.format(field))
        return self
