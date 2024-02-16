"""Module Notification."""


class Notification:
	"""Class Notification."""

	def __init__(self, field: str, message: str) -> None:
		"""Found 'Constructor'."""
		self.field: str = field
		self.message: str = message

	def __str__(self):
		"""Print object string."""
		string = '{}field: {}, message: {}{}'
		return string.format('{', self.field, self.message, '}')
