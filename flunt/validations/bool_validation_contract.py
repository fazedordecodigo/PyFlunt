"""Module Contract."""

from __future__ import annotations

from typing import Self

from flunt.constants.messages import IS_FALSE, IS_TRUE
from flunt.notifications.notifiable import Notifiable


class BoolValidationContract(Notifiable):
    """
    Bool Validation Contract.

    This class provides methods for validating boolean values and adding notifications based on the validation results.

    Methods
    -------
    is_false(value: bool, field: str, message: str) -> self:
            Checks if the provided boolean value is False and adds a notification if it is True.

    is_true(value: bool, field: str, message: str) -> self:
            Checks if the provided boolean value is True and adds a notification if it is False.

    """

    def is_false(
        self, value: bool, field: str, message: str = IS_FALSE
    ) -> Self:
        """
        Check if the provided boolean value is False and adds a notification if it is True.

        Parameters
        ----------
        `value`: bool
                The boolean value to be checked.
        `field`: str
                The field or identifier associated with the notification.
        `message`: str
                The message of the notification to be added.

        Returns
        -------
        `Self`
        The current instance of the class.

        Notes
        -----
        - If the provided `value` is ``True``, a notification is added to the current
        instance using the provided `field` and `message`.
        - If the provided `value` is ``False``, no notification is added.

        Examples
        --------
        ```python
        obj = Contract()
                .is_false(False, "BoolCheck", "Value should return true")
        obj.is_valid # True
        ```

        """
        if message is IS_FALSE:
            message = IS_FALSE.format(field)
        
        if value:
            self.add_notification(field, message)
        return self

    def is_true(self, value: bool, field: str, message: str = IS_TRUE) -> Self:
        """
        Check if the provided boolean value is True and adds a notification if it is True.

        Parameters
        ----------
        `value`: bool
                The boolean value to be checked.
        `field`: str
                The field or identifier associated with the notification.
        `message`: str
                The message of the notification to be added.

        Returns
        -------
        `Self`
        The current instance of the class.

        Notes
        -----
        - If the provided `value` is ``False``, a notification is added to the current
        instance using the provided `field` and `message`.
        - If the provided `value` is ``True``, no notification is added.

        Examples
        --------
        ```python
        obj = Contract()
                .is_true(True, "BoolCheck", "Value should return true")
        obj.is_valid # True
        ```

        """
        if message is IS_TRUE:
            message = IS_TRUE.format(field)
        if not value:
            self.add_notification(field, message)
        return self
