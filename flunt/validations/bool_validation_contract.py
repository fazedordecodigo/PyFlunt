"""Module Contract."""
from typing_extensions import Self

from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class BoolValidationContract(Notifiable):
	"""
	Bool Validation Contract.

	This class provides methods for validating boolean values and adding notifications based on the validation results.

	Methods:
	-------
	is_false(value: bool, key: str, message: str) -> self:
	        Checks if the provided boolean value is False and adds a notification if it is True.

	is_true(value: bool, key: str, message: str) -> self:
	        Checks if the provided boolean value is True and adds a notification if it is False.

	"""

	def is_false(self, value: bool, key: str, message: str) -> Self:
		"""
		Check if the provided boolean value is False and adds a notification if it is True.

		Parameters
		----------
		`value`: bool
		The boolean value to be checked.
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
		- If the provided `value` is ``True``, a notification is added to the current
		instance using the provided `key` and `message`.
		- If the provided `value` is ``False``, no notification is added.

		Examples:
		--------
		```python
		obj = Contract()
		              .is_false(False, "BoolCheck", "Value should return true")
		obj.is_valid # True
		```

		"""
		if value:
			self.add_notification(Notification(key, message))

		return self

	def is_true(self, value: bool, key: str, message: str) -> Self:
		"""
		Check if the provided boolean value is True and adds a notification if it is True.

		Parameters
		----------
		`value`: bool
		The boolean value to be checked.
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
		- If the provided `value` is ``False``, a notification is added to the current
		instance using the provided `key` and `message`.
		- If the provided `value` is ``True``, no notification is added.

		Examples:
		--------
		```python
		obj = Contract()
		              .is_true(True, "BoolCheck", "Value should return true")
		obj.is_valid # True
		```

		"""
		if not value:
			self.add_notification(Notification(key, message))

		return self
