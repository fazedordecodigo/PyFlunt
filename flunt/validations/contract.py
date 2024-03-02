"""Module Contract."""

from typing_extensions import Self

from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification
from flunt.validations.bool_validation_contract import BoolValidationContract
from flunt.validations.commons_validation_contract import CommonsValidationContract
from flunt.validations.credit_card_validation_contract import (
	CreditCardValidationContract,
)
from flunt.validations.email_validation_contract import EmailValidationContract
from flunt.validations.strings_validation_contract import StringValidationContract


class Contract(
	StringValidationContract,
	EmailValidationContract,
	BoolValidationContract,
	CreditCardValidationContract,
	CommonsValidationContract,
	Notifiable,
):
	"""
	Class represents a contract for validating data..

	Parameters:
	-----------
	    N/A

	Attributes:
	----------
	    N/A

	Methods:
	-------
	- requires(value, key: str, message: str): Checks if the given value is empty and adds a notification if it is.

	"""

	def requires(self, value, key: str, message: str) -> Self:
		"""
		Check if the given value is empty and adds a notification if it is.

		Parameters:
		-----------
		`value`
		    The value to be checked.
		`key`: str
		    The key or identifier associated with the notification.
		`message`: str
		    The message of the notification to be added.

		Returns:
		-------
		`Self`
		    The current instance of the class.

		Notes:
		-----
		- If the provided `value` is empty, a `notification` is added to the current
		instance using the provided `key` and `message`.
		- If the provided `value` is not empty, no `notification` is added.

		Examples:
		--------
		```python
		contract = Contract().requires('', 'key', 'message')
		contract.is_valid  # False
		```

		"""
		if value is None:
			self.add_notification(Notification(key, message))

		if not value:
			self.add_notification(Notification(key, message))

		return self
