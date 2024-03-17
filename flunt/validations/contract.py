"""Module Contract."""

from collections.abc import Iterable
from decimal import Decimal
from struct import Struct
from typing import Callable, Union, overload
from uuid import UUID

from typing_extensions import Self

from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification
from flunt.validations.bool_validation_contract import BoolValidationContract
from flunt.validations.collections_validation_contract import (
	CollectionsValidationContract,
)
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
	CollectionsValidationContract,
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

	@overload
	def requires(self, value: tuple, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: Struct, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: set, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: bool, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: dict, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: list, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: Iterable, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: Callable, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: int, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: str, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: Decimal, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: float, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: UUID, key: str, message: str) -> Self:
		...

	@overload
	def requires(self, value: object, key: str, message: str) -> Self:
		...

	def requires(
		self,
		value: Union[
			str,
			int,
			list,
			bool,
			Decimal,
			float,
			UUID,
			dict,
			object,
			set,
			Struct,
			tuple,
			Iterable,
			Callable,
		],
		key: str,
		message: str,
	) -> Self:
		"""
		Check if the given value is empty and adds a notification if it is.

		Parameters:
		-----------
		`value`: [bool | str | float | int | Tuple | Set | List | Iterable | Dict | Callable | Decimal | UUID | object | Struct]
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
		if not value and not isinstance(value, bool):
			self.add_notification(Notification(key, message))

		return self
