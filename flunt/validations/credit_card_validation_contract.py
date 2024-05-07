"""Module Contract."""

import re

from typing_extensions import Self

from flunt.constants.messages import IS_NOT_CREDIT_CARD
from flunt.localization.flunt_regex_patterns import FluntRegexPatterns
from flunt.notifications.notifiable import Notifiable


class CreditCardValidationContract(Notifiable):
    """
    Credit Card Validation Contract.

    This class provides methods for validating Credit Card values and adding notifications
    based on the validation results.

    Methods
    -------
    is_credit_card(self, value: bool, field: str, message: str) -> self:
            Checks if the provided str value is a Credt Card Number and adds a notification if it is not True.

    """

    def is_credit_card(
        self, value: str, field: str, message: str = IS_NOT_CREDIT_CARD
    ) -> Self:
        """
        Check if the provided str value is a Credt Card Number and adds a notification if it is not True.

        Parameters
        ----------
        `value`: str
                The string value to be checked.
        `field`: str
                The field or identifier associated with the notification.
        `message`: str (optional)
                The message of the notification to be added.

        Returns
        -------
        `self`
                The current instance of the class.

        Notes
        -----
        - If the provided `value` is not a Credit Card Number, a `notification` is added
        to the current instance using the provided `field` and `message`.
        - If the provided `value` is a Credit Card Number, no `notification` is added.

        Examples
        --------
        ```python
        obj = Contract()
                .is_credit_card("5432.5678.3234.2343", "CreditCard", "Value should return a valid Credit Card Number")
        obj.is_valid # True
        ```

        """
        if not re.match(
            FluntRegexPatterns().only_number_regex_pattern,
            value,
            re.IGNORECASE,
        ):
            self.add_notification(field, message.format(field))
            return self

        even = False
        checksum = 0

        for digit in reversed(value):
            if not digit.isdigit():
                self.add_notification(field, message.format(field))
                return self

            val = int(digit) * (2 if even else 1)
            even = not even

            while val > 0:
                checksum += val % 10
                val //= 10

        if checksum % 10 != 0:
            self.add_notification(field, message.format(field))
        return self
