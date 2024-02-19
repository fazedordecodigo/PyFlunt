"""Module Notifiable."""

from flunt.notifications.notification import Notification


class Notifiable(Notification):
	"""
	A class representing an object that can be notified.

	This class extends Notification and provides methods for managing notifications.

	Attributes:
	----------
	notifications: list[Notification]
	    A list of notifications.
	is_valid: bool
	    A boolean indicating if there are any notifications.

	Methods:
	-------
	- get_notification_instance
	- add_notifications
	- add_notification
	- get_notifications
	- clear
	"""

	def __init__(self) -> None:
		"""Initialize the Notifiable object."""
		self._notifications: list[Notification] = []

	@property
	def notifications(self) -> list[Notification]:
		"""
		Return the list of notifications.

		Returns:
		-------
		`list[Notification]`
		    A list of notifications.

		Examples:
		--------
		```python
		obj = Notifiable()
		obj.notifications  # []
		```
		"""
		return self._notifications

	@property
	def is_valid(self) -> bool:
		"""
		Check if there are any notifications.

		Returns:
		-------
		`bool`
		    True if there are no notifications, False otherwise.

		Examples:
		--------
		```python
		obj = Notifiable()
		obj.is_valid()  # True
		```
		"""
		return not self._notifications

	def get_notification_instance(self, key: str, message: str) -> Notification:
		"""
		Return a new instance of Notification.

		Parameters:
		-----------
		`key`: str
		    The key of the notification.
		`message`: str
		    The message of the notification.

		Returns:
		-------
		`Notification`
		    A new instance of Notification.

		Examples:
		--------
		```python
		obj = Notifiable()
		obj.get_notification_instance(
		    'key', 'message'
		)
		obj.notifications  # [Notification("key", "message")]
		```
		"""
		return Notification(key, message)

	def add_notifications(self, notifications: list[Notification]) -> None:
		"""
		Add notifications from a list of contracts to the list of notifications.

		Parameters:
		-----------
		`notifications`: list[Notification]
		    A list of notifications to be added.

		Returns:
		-------
		`None`

		Examples:
		--------
		```python
		obj = Notifiable()
		obj.add_notifications(
		    [
		        Notification(
		            'key', 'message'
		        )
		    ]
		)
		obj.notifications  # [Notification("key", "message")]
		```
		"""
		self._notifications.extend(notifications)

	def add_notification(self, notification: Notification) -> None:
		"""
		Add a single notification to the list of notifications.

		Parameters:
		-----------
		`notification`: Notification
		    The notification to be added.

		Returns:
		-------
		`None`

		Examples:
		--------
		```python
		obj = Notifiable()
		obj.add_notification(
		    Notification(
		        'key', 'message'
		    )
		)
		obj.notifications  # [Notification("key", "message")]
		```
		"""
		self._notifications.append(notification)

	def get_notifications(self) -> list[Notification]:
		"""
		Return the list of notifications.

		Returns:
		-------
		`list[Notification]`
		    A list of notifications.

		Examples:
		--------
		```python
		obj = Notifiable()
		obj.get_notifications()  # []
		```
		"""
		return self._notifications

	def clear(self) -> None:
		"""
		Clear the list of notifications.

		Returns:
		-------
		`None`

		Examples:
		--------
		```python
		obj = Notifiable()
		obj.clear()  # []
		```
		"""
		self._notifications.clear()

	def __str__(self) -> str:
		"""
		Return a string representation of the list of notifications.

		Returns:
		-------
		`str`
		    A string representation of the list of notifications.

		Examples:
		--------
		```python
		obj = Notifiable()
		obj.__str__()
		"""
		return self._notifications.__str__()
