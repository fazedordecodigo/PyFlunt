"""Module Contract."""

from typing_extensions import Self

from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class CommonsValidationContract(Notifiable):
	"""
	Class for validating values and adding notifications based on various comparisons.

	Parameters
	----------
	    N/A

	Attributes:
	----------
	    N/A

	Methods:
	-------
	- is_none(value, key: str, message: str): Checks if a value is None.
	- is_not_none(value, key: str, message: str): Checks if a value is not None.
	- are_equals(value, comparer, key: str, message: str): Checks if two values are equal.
	- are_not_equals(value, comparer, key: str, message: str): Checks if two values are not equal.

	"""

	def is_none(self, value, key: str, message: str) -> Self:
		"""
		Check if a string value is not None and adds a notification if it is.

		Parameters
		----------
		`value`
		    The value to be checked.
		`key`: str
		    The key or identifier associated with the check.
		`message`: str
		    The notification message to be added if the value is None.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is not None, no notification is added.
		- If the `value` is None, a notification is added to the current instance with the provided `key` and `message`.

		Examples:
		--------
		```python
		obj = Contract()
		      .is_none("Hello", "ValueCheck", "Value should not be None")
		obj.is_valid
		```

		"""
		if value is not None:
			self.add_notification(Notification(key, message))

		return self

	def is_not_none(self, value, key: str, message: str) -> Self:
		"""
		Check if a value is not None and adds a notification if it is.

		Parameters
		----------
		`value`
		    The value to be checked.
		`key`: str
		    The key or identifier associated with the check.
		`message`: str
		    The notification message to be added if the value is None.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is None, a notification is added to the current instance with the provided `key` and `message`.
		- If the `value` is not None, no notification is added.

		Examples:
		--------
		```python
		obj = Contract()
		      .is_not_none("Hello", "ValueCheck", "Value should not be None")
		obj.is_valid
		```

		"""
		if value is None:
			self.add_notification(Notification(key, message))

		return self

	def are_equals(self, value: str, comparer: str, key: str, message: str) -> Self:
		"""
		Check if two string values are equal and adds a notification if they are not equal.

		Parameters
		----------
		`value`: str
		    The first string value to compare.
		`comparer`: str
		    The second string value to compare with the first value.
		`key`: str
		    The key or identifier associated with the comparison.
		`message`: str
		    The notification message to be added if the values are not equal.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is not equal to `comparer`, a notification is added to the current instance
		with the provided `key` and `message`. Otherwise, no notification is added.

		Examples:
		--------
		```python
		obj = Contract()
		      .are_equals("Hello", "Hello", "Comparison", "Values should be equal")
		obj.is_valid
		```

		"""
		if value != comparer:
			self.add_notification(Notification(key, message))

		return self

	def are_not_equals(self, value: str, comparer: str, key: str, message: str) -> Self:
		"""
		Require two strings are not equals.

		Parameters
		----------
		`value`: str
		    The value to be compared.
		`comparer`: str
		    The value to compare with `value`.
		`key`: str
		    The key or identifier related to the comparison.
		`message`: str
		    The notification message in case of equal values.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is equal to `comparer`, a notification is added to the current instance
		with the provided `key` and `message`. Otherwise, no notification is added.

		Examples:
		--------
		```python
		obj = Contract()
		      .are_not_equals("Hello", "World", "Comparison", "Values should not be equal")
		obj.is_valid
		```

		"""
		if value == comparer:
			self.add_notification(Notification(key, message))

		return self
