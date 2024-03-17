"""Module Contract."""
from typing import Union, overload

from typing_extensions import Self

from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class CollectionsValidationContract(Notifiable):
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
	- is_lower_than(value, comparer, key, message): Checks if the length of a collection value is lower than a given number.
	- is_lower_or_equals_than(value, comparer, key, message): Checks if the length of a collection value is lower or equal to a given number.
	- is_greater_than(value, comparer, key, message): Checks if the length of a collection value is greater than a given number.
	- is_greater_or_equals_than(value, comparer, key, message): Checks if the length of a collection value is greater or equal to a given number.
	- contains(value, comparer, key, message): Checks if a collection contains a specific collection.
	- not_contains(value, comparer, key, message): Checks if a collection does not contain a specific collection.
	- is_between(value, min, max, key, message): Checks if the length of a colection is between a minimum and maximum value.

	"""

	@overload
	def is_lower_than(self, value: bytearray, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_than(self, value: range, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_than(self, value: tuple, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_than(self, value: set, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_than(self, value: dict, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_than(self, value: list, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_than(self, value: str, comparer: int, key: str, message: str) -> Self:
		...
	def is_lower_than(self, value: Union[str, list, dict, set, tuple, range, bytearray], comparer: int, key: str, message: str) -> Self:
		"""
		Check if the length of a collection value is lower than a given number and adds a notification if it's greater.

		Parameters
		----------
		`value`: str | list | dict | set | tuple | range | bytearray
		    The collection value to compare.
		`comparer`: int
		    The maximum length allowed for the value.
		`key`: str
		    The key or identifier associated with the comparison.
		`message`: str
		    The notification message to be added if the length exceeds the comparer.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is an empty string or None, no notification is added.
		- If the length of `value` is greater than `comparer`, a notification is added to the current instance
		with the provided `key` and `message`.

		Examples:
		--------
		```python
		obj = Contract()
		      .is_lower_than("Hello", 10, "LengthCheck", "Value should have a length less than 10")
		obj.is_valid
		```

		"""
		if not value:
			return self

		if not hasattr(value, '__iter__'):
			self.add_notification(Notification(key, "Value is not iterable"))
			return self

		if len(value) >= comparer:
			self.add_notification(Notification(key, message))

		return self

	@overload
	def is_lower_or_equals_than(self, value: bytearray, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_or_equals_than(self, value: range, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_or_equals_than(self, value: tuple, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_or_equals_than(self, value: set, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_or_equals_than(self, value: dict, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_or_equals_than(self, value: list, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_lower_or_equals_than(self, value: str, comparer: int, key: str, message: str) -> Self:
		...
	def is_lower_or_equals_than(
		self, value: Union[str, list, dict, set, tuple, range, bytearray], comparer: int, key: str, message: str
	) -> Self:
		"""
		Check if the length of a collection value is lower or equal to a given number and adds a notification if it exceeds.

		Parameters
		----------
		`value`: str | list | dict | set | tuple | range | bytearray
		    The collection value to compare.
		`comparer`: int
		    The maximum length allowed for the value.
		`key`: str
		    The key or identifier associated with the comparison.
		`message`: str
		    The notification message to be added if the length exceeds the comparer.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is an empty string or None, no notification is added.
		- If the length of `value` is greater than or equal to `comparer`, a notification is added to the current instance
		with the provided `key` and `message`.

		Examples:
		--------
		```python
		obj = Contract()
		      .is_lower_or_equals_than("Hello", 10, "LengthCheck", "Value should have a length less than or equal to 10")
		obj.is_valid
		```

		"""
		if not value:
			return self

		if not hasattr(value, '__iter__'):
			self.add_notification(Notification(key, "Value is not iterable"))
			return self

		if len(value) > comparer:
			self.add_notification(Notification(key, message))

		return self

	@overload
	def is_greater_than(self, value: bytearray, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_than(self, value: range, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_than(self, value: tuple, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_than(self, value: set, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_than(self, value: dict, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_than(self, value: list, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_than(self, value: str, comparer: int, key: str, message: str) -> Self:
		...
	def is_greater_than(
		self, value: Union[str, list, dict, set, tuple, range, bytearray], comparer: int, key: str, message: str
	) -> Self:
		"""
		Check if the length of a collection value is greater than a given number and adds a notification if it's smaller.

		Parameters
		----------
		`value`: str | list | dict | set | tuple | range | bytearray
		    The collection value to compare.
		`comparer`: int
		    The minimum length required for the value.
		`key`: str
		    The key or identifier associated with the comparison.
		`message`: str
		    The notification message to be added if the length is smaller than the comparer.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is an empty string or None, no notification is added.
		- If the length of `value` is smaller than `comparer`, a notification is added to the current instance
		with the provided `key` and `message`.

		Examples:
		--------
		```python
		obj = Contract()
		      .is_greater_than("Hello", 3, "LengthCheck", "Value should have a length greater than 3")
		obj.is_valid
		```

		"""
		if not value:
			return self

		if not hasattr(value, '__iter__'):
			self.add_notification(Notification(key, "Value is not iterable"))
			return self

		if len(value) <= comparer:
			self.add_notification(Notification(key, message))

		return self

	@overload
	def is_greater_or_equals_than(self, value: bytearray, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_or_equals_than(self, value: range, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_or_equals_than(self, value: tuple, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_or_equals_than(self, value: set, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_or_equals_than(self, value: dict, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_or_equals_than(self, value: list, comparer: int, key: str, message: str) -> Self:
		...
	@overload
	def is_greater_or_equals_than(self, value: str, comparer: int, key: str, message: str) -> Self:
		...
	def is_greater_or_equals_than(
		self, value: Union[str, list, dict, set, tuple, range, bytearray], comparer: int, key: str, message: str
	) -> Self:
		"""
		Check if the length of a collection value is greater than or equal to a given number and adds a notification if it's smaller.

		Parameters
		----------
		`value`: str | list | dict | set | tuple | range | bytearray
		    The collection value to compare.
		`comparer`: int
		    The minimum length required for the value.
		`key`: str
		    The key or identifier associated with the comparison.
		`message`: str
		    The notification message to be added if the length is smaller than the comparer.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is an empty string or None, no notification is added.
		- If the length of `value` is smaller than or equal to `comparer`, a notification is added to the current instance
		with the provided `key` and `message`.

		Example:
		--------
		```python
		obj = Contract()
		      .is_greater_or_equals_than("Hello", 3, "LengthCheck", "Value should have a length greater than or equal to 3")
		obj.is_valid
		```

		"""
		if not value:
			return self

		if not hasattr(value, '__iter__'):
			self.add_notification(Notification(key, "Value is not iterable"))
			return self

		if len(value) < comparer:
			self.add_notification(Notification(key, message))

		return self

	@overload
	def contains(self, value: bytearray, comparer: bytearray, key: str, message: str) -> Self:
		...
	@overload
	def contains(self, value: range, comparer: range, key: str, message: str) -> Self:
		...
	@overload
	def contains(self, value: tuple, comparer: tuple, key: str, message: str) -> Self:
		...
	@overload
	def contains(self, value: set, comparer: set, key: str, message: str) -> Self:
		...
	@overload
	def contains(self, value: dict, comparer: dict, key: str, message: str) -> Self:
		...
	@overload
	def contains(self, value: list, comparer: list, key: str, message: str) -> Self:
		...
	@overload
	def contains(self, value: str, comparer: str, key: str, message: str) -> Self:
		...
	def contains(
			self,
			value: Union[
				str,
				list,
				dict,
				set,
				tuple,
				range,
				bytearray
			],
			comparer: Union[
				str,
				list,
				dict,
				set,
				tuple,
				range,
				bytearray
			],
			key: str,
			message: str
		) -> Self:
		"""
		Check if a collection value contains another collection and adds a notification if it does.

		Parameters
		----------
		`value`: str | list | dict | set | tuple | range | bytearray
		    The collection value to be checked.
		`comparer`: str | list | dict | set | tuple | range | bytearray
		    The collection to search for within the value.
		`key`: str
		    The key or identifier associated with the check.
		`message`: str
		    The notification message to be added if the value contains the comparer.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` contains the `comparer` collection, a notification is added to the current instance
		with the provided `key` and `message`.
		- If the `value` does not contain the `comparer` collection, no notification is added.

		Examples:
		--------
		```python
		obj = Contract()
		      .contains("Hello, world!", "world", "ContainsCheck", "Value should contain 'world'")
		obj.is_valid
		```

		"""
		if not hasattr(value, '__iter__'):
			self.add_notification(Notification(key, "Value is a not collection"))
			return self

		if isinstance(value, str) and isinstance(comparer, str) :
			if value.find(comparer) == -1:
				self.add_notification(Notification(key, message))
				return self

		if isinstance(value, (list, set, tuple, range)) and isinstance(comparer, (list, set, tuple, range)):
			if comparer in value:
				self.add_notification(Notification(key, message))
				return self

		if isinstance(value, bytearray) and isinstance(comparer, bytearray):
			if comparer in value:
				self.add_notification(Notification(key, message))
				return self

		if isinstance(value, dict) and comparer in value.keys():
			self.add_notification(Notification(key, message))

		return self

	@overload
	def not_contains(self, value: bytearray, comparer: bytearray, key: str, message: str) -> Self:
		...
	@overload
	def not_contains(self, value: range, comparer: range, key: str, message: str) -> Self:
		...
	@overload
	def not_contains(self, value: tuple, comparer: tuple, key: str, message: str) -> Self:
		...
	@overload
	def not_contains(self, value: set, comparer: set, key: str, message: str) -> Self:
		...
	@overload
	def not_contains(self, value: dict, comparer: dict, key: str, message: str) -> Self:
		...
	@overload
	def not_contains(self, value: list, comparer: list, key: str, message: str) -> Self:
		...
	@overload
	def not_contains(self, value: str, comparer: str, key: str, message: str) -> Self:
		...
	def not_contains(
			self,
			value: Union[
				str,
				list,
				dict,
				set,
				tuple,
				range,
				bytearray
			],
			comparer: Union[
				str,
				list,
				dict,
				set,
				tuple,
				range,
				bytearray
			],
			key: str,
			message: str
		) -> Self:
		"""
		Check if a collection value does not contain a specified collection and adds a notification if it does.

		Parameters
		----------
		`value`: str | list | dict | set | tuple | range | bytearray
		    The collection value to be checked.
		`comparer`: str | list | dict | set | tuple | range | bytearray
		    The collection to search for in the value.
		`key`: str
		    The key or identifier associated with the check.
		`message`: str
		    The notification message to be added if the value contains the comparer.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` does not contain the `comparer` collection, no notification is added.
		- If the `value` contains the `comparer` collection, a notification is added to the current instance
		with the provided `key` and `message`.

		Examples:
		--------
		```python
		obj = Contract()
		      .not_contains("Hello", "World", "Comparison", "Value should not contain 'World'")
		obj.is_valid
		```

		"""
		if not hasattr(value, '__iter__'):
			self.add_notification(Notification(key, "Value is a not collection"))
			return self

		if isinstance(value, str) and isinstance(comparer, str) :
			if value.find(comparer) != -1:
				self.add_notification(Notification(key, message))
				return self

		if isinstance(value, (list, set, tuple, range)) and isinstance(comparer, (list, set, tuple, range)):
			if comparer not in value:
				self.add_notification(Notification(key, message))
				return self

		if isinstance(value, bytearray) and isinstance(comparer, bytearray):
			if comparer not in value:
				self.add_notification(Notification(key, message))
				return self

		if isinstance(value, dict) and comparer not in value.keys():
			self.add_notification(Notification(key, message))

		return self

	@overload
	def is_between(self, value: bytearray, min: int, max: int, key: str, message: str) -> Self:
		...
	@overload
	def is_between(self, value: range, min: int, max: int, key: str, message: str) -> Self:
		...
	@overload
	def is_between(self, value: tuple, min: int, max: int, key: str, message: str) -> Self:
		...
	@overload
	def is_between(self, value: set, min: int, max: int, key: str, message: str) -> Self:
		...
	@overload
	def is_between(self, value: dict, min: int, max: int, key: str, message: str) -> Self:
		...
	@overload
	def is_between(self, value: list, min: int, max: int, key: str, message: str) -> Self:
		...
	@overload
	def is_between(self, value: str, min: int, max: int, key: str, message: str) -> Self:
		...
	def is_between(
		self, value: Union[str, list, dict, set, tuple, range, bytearray], min: int, max: int, key: str, message: str
	) -> Self:
		"""
		Require a collection value to have a length between a minimum and maximum value (inclusive), and adds a notification if the length is outside the specified range.

		Parameters
		----------
		`value`: str | list | dict | set | tuple | range | bytearray
		    The collection value to be checked.
		`min`: int
		    The minimum allowed length for the value.
		`max`: int
		    The maximum allowed length for the value.
		`key`: str
		    The key or identifier associated with the length check.
		`message`: str
		    The notification message to be added if the length is outside the range.

		Returns:
		-------
		`self`
		    The current instance with potential notifications added.

		Notes:
		-----
		- If the `value` is empty, the function returns the current instance without adding any notifications.
		- If the `value` is None or consists only of whitespace characters, the function returns the current instance without adding any notifications.
		- If the length of `value` is less than `min` or greater than `max`, a notification is added to the current instance
		with the provided `key` and `message`.

		Examples:
		--------
		```python
		obj = Contract()
		      .is_between("Hello", 3, 6, "LengthCheck", "Value length should be between 3 and 6")
		obj.is_valid
		```

		"""
		if not value:
			return self

		if not hasattr(value, '__iter__'):
			self.add_notification(Notification(key, "Value is a not collection"))
			return self

		if len(value) < min or len(value) > max:
			self.add_notification(Notification(key, message))

		return self
