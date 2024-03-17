"""Module Contract."""

from typing_extensions import Self

from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class StringValidationContract(Notifiable):
	"""
	Class for validating string values and adding notifications based on various comparisons.

	Parameters
	----------
	    N/A

	Attributes:
	----------
	    N/A

	Methods:
	-------
	- is_not_none_or_white_space(value, key, message): Checks if a string value is not None or whitespace.

	"""

	def is_not_none_or_white_space(self, value: str, key: str, message: str) -> Self:
		"""
		Check if a string value is not None or whitespace and adds a notification if it is.

		Parameters
		----------
		`value`: str
		    The string value to be checked.
		`key`: str
		    The key or identifier associated with the check.
		`message`: str
		    The notification message to be added if the value is None or whitespace.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is None or consists only of whitespace characters (spaces, tabs, newlines, etc.),
		a notification is added to the current instance with the provided `key` and `message`.
		- If the `value` is not None and contains at least one non-whitespace character, no notification is added.

		Examples:
		--------
		```python
		obj = Contract()
		      .is_not_none_or_white_space("Hello", "ValueCheck", "Value should not be None or whitespace")
		obj.is_valid
		```

		"""
		if value is None or value.isspace():
			self.add_notification(Notification(key, message))

		return self
