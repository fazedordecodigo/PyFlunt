"""Module Email Validation Contract."""

import re
from typing import Union

from typing_extensions import Self

from flunt.localization.flunt_regex_patterns import FluntRegexPatterns
from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class EmailValidationContract(Notifiable):
	"""
	Email Validation Contract.

	This class provides methods for validating email addresses and adding notifications based on the validation results.

	Methods:
	-------
	is_email(value: str, key: str, message: str) -> self:
	    Checks if the provided value is a valid email address and adds a notification if it is not.

	is_not_email(value: str, key: str, message: str) -> self:
	    Checks if the provided value is not a valid email address and adds a notification if it is.

	Notes:
	-----
	The validity of the email address is determined by the internal method `_valid_email`.

	"""

	def is_email(self, value: str, key: str, message: str) -> Self:
		"""
		Check if the provided value is a valid email address and adds a notification if it is not.

		Parameters
		----------
		`value`: str
		    The value to be checked as an email address.
		`key`: str
		    The key or identifier associated with the notification.
		`message`: str
		    The message of the notification to be added.

		Returns:
		-------
		`self`
		    The current instance of the class.

		Notes:
		-----
		- The validity of the email address is determined by the internal method `_valid_email`.
		- If the provided `value` is not a valid email address, a `notification` is added to the current instance
		using the provided key and message.
		- If the provided `value` is a valid email address, no `notification` is added.

		Examples:
		--------
		```python
		obj = Contract()
		      .is_email("example@example.com", "EmailCheck", "Please enter a valid email address")
		obj.is_valid # True
		```

		"""
		if not self._valid_email(value):
			self.add_notification(Notification(key, message))

		return self

	def is_not_email(self, value: str, key: str, message: str) -> Self:
		"""
		Check if the provided value is not a valid email address and adds a notification if it is.

		Parameters
		----------
		`value`: str
		    The value to be checked as an email address.
		`key`:str
		    The key or identifier associated with the notification.
		`message`: str
		    The message of the notification to be added.

		Returns:
		-------
		`self`
		    The current instance of the class.

		Notes:
		-----
		- If the provided `value` matches the valid email address pattern, a `notification`
		is added to the current instance using the provided `key` and `message`.
		- If the provided `value` does not match the valid email address pattern, no `notification` is added.

		Examples:
		--------
		```python
		obj = Contract()
		      .is_not_email("example@example.com", "EmailCheck", "Value should not be a valid email address")
		obj.is_valid # False
		```

		"""
		if self._valid_email(value):
			self.add_notification(Notification(key, message))

		return self

	def _valid_email(self, value) -> Union[re.Match[str], None]:
		"""
		Check if the provided value matches the valid email address pattern.

		Parameters
		----------
		`value`: str
		    The value to be checked as an email address.

		Returns:
		-------
		`(Match[str] | None)`

		"""
		return re.match(
			FluntRegexPatterns().email_regex_pattern,
			value,
			re.IGNORECASE,
		)
