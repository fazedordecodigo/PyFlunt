"""Module Contract."""

from collections.abc import Iterable
from decimal import Decimal
from struct import Struct
from typing import Callable, Union, overload
from uuid import UUID

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
	- is_none(value: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct], key: str, message: str): Checks if a value is None.
	- is_not_none(value: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct], key: str, message: str): Checks if a value is not None.
	- are_equals(value: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct], comparer: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct], key: str, message: str): Checks if two values are equal.
	- are_not_equals(value: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct], comparer: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct], key: str, message: str): Checks if two values are not equal.

	"""

	@overload
	def is_none(self, value: tuple, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: Struct, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: set, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: bool, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: dict, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: list, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: Iterable, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: Callable, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: int, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: str, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: Decimal, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: float, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: UUID, key: str, message: str) -> Self:
		...

	@overload
	def is_none(self, value: object, key: str, message: str) -> Self:
		...

	def is_none(
		self,
		value: Union[
			str,
			int,
			list,
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
			bool,
		],
		key: str,
		message: str,
	) -> Self:
		"""
		Check if value is not None and adds a notification if it is.

		Parameters
		----------
		`value`: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct]
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

	@overload
	def is_not_none(self, value: tuple, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: Struct, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: set, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: bool, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: dict, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: list, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: Iterable, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: Callable, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: int, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: str, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: Decimal, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: float, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: UUID, key: str, message: str) -> Self:
		...

	@overload
	def is_not_none(self, value: object, key: str, message: str) -> Self:
		...

	def is_not_none(
		self,
		value: Union[
			str,
			int,
			list,
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
			bool,
		],
		key: str,
		message: str,
	) -> Self:
		"""
		Check if a value is not None and adds a notification if it is.

		Parameters
		----------
		`value`: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct]
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

	@overload
	def are_equals(self, value: tuple, comparer: tuple, key: str, message: str) -> Self:
		...

	@overload
	def are_equals(
		self, value: Struct, comparer: Struct, key: str, message: str
	) -> Self:
		...

	@overload
	def are_equals(self, value: set, comparer: set, key: str, message: str) -> Self:
		...

	@overload
	def are_equals(self, value: bool, comparer: bool, key: str, message: str) -> Self:
		...

	@overload
	def are_equals(self, value: dict, comparer: dict, key: str, message: str) -> Self:
		...

	@overload
	def are_equals(self, value: list, comparer: list, key: str, message: str) -> Self:
		...

	@overload
	def are_equals(
		self, value: Iterable, comparer: Iterable, key: str, message: str
	) -> Self:
		...

	@overload
	def are_equals(
		self, value: Callable, comparer: Callable, key: str, message: str
	) -> Self:
		...

	@overload
	def are_equals(self, value: int, comparer: int, key: str, message: str) -> Self:
		...

	@overload
	def are_equals(self, value: str, comparer: str, key: str, message: str) -> Self:
		...

	@overload
	def are_equals(
		self, value: Decimal, comparer: Decimal, key: str, message: str
	) -> Self:
		...

	@overload
	def are_equals(self, value: float, comparer: float, key: str, message: str) -> Self:
		...

	@overload
	def are_equals(self, value: UUID, comparer: UUID, key: str, message: str) -> Self:
		...

	@overload
	def are_equals(
		self, value: object, comparer: object, key: str, message: str
	) -> Self:
		...

	def are_equals(
		self,
		value: Union[
			str,
			int,
			list,
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
			bool,
		],
		comparer: Union[
			str,
			int,
			list,
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
			bool,
		],
		key: str,
		message: str,
	) -> Self:
		"""
		Check if two string values are equal and adds a notification if they are not equal.

		Parameters
		----------
		`value`: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct]
		    The first value to compare.
		`comparer`: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct]
		    The second value to compare with the first value.
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

	@overload
	def are_not_equals(
		self, value: tuple, comparer: tuple, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: Struct, comparer: Struct, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(self, value: set, comparer: set, key: str, message: str) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: bool, comparer: bool, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: dict, comparer: dict, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: list, comparer: list, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: Iterable, comparer: Iterable, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: Callable, comparer: Callable, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(self, value: int, comparer: int, key: str, message: str) -> Self:
		...

	@overload
	def are_not_equals(self, value: str, comparer: str, key: str, message: str) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: Decimal, comparer: Decimal, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: float, comparer: float, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: UUID, comparer: UUID, key: str, message: str
	) -> Self:
		...

	@overload
	def are_not_equals(
		self, value: object, comparer: object, key: str, message: str
	) -> Self:
		...

	def are_not_equals(
		self,
		value: Union[
			str,
			int,
			list,
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
			bool,
		],
		comparer: Union[
			str,
			int,
			list,
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
			bool,
		],
		key: str,
		message: str,
	) -> Self:
		"""
		Require two values are not equals.

		Parameters
		----------
		`value`: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct]
		    The value to be compared.
		`comparer`: [bool | str | float | int | tuple | set | list | Iterable | dict | Callable | Decimal | UUID | object | Struct]
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
