from flunt.constants import MAX_LENGTH, REQUIRED


def required(field: str):
	"""
	Returns the error message for a required field.

	Args:
	    field (str): The name of the required field.

	Returns:
	    str: The error message.

	"""
	return REQUIRED.format(field)


def max_length(field: str, max: int):
	"""
	Returns a formatted error message for a maximum length validation.

	Args:
	    field (str): The name of the field being validated.
	    max (int): The maximum length allowed for the field.

	Returns:
	    str: The formatted error message.

	"""
	return MAX_LENGTH.format(field, max)
