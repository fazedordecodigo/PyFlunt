"""Module Notification."""

class Notification:
	"""Class Notification."""

	def __init__(self, field: str, message: str) -> None:
		"""Found 'Constructor'."""
		self.field: str = field
		self.message: str = message

	def __repr__(self):
		"""Representation object string."""
		return f"{{ field: {self.field}, message: {self.message} }}"
