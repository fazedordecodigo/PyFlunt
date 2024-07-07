from flunt.constants import MAX_LENGTH, REQUIRED

IS_URL_ERROR_MESSAGE = lambda key: f"{key} is not a valid URL."
IS_URL_OR_EMPTY_ERROR_MESSAGE = lambda key: f"{key} is not a valid URL or empty."
IS_NOT_URL_ERROR_MESSAGE = lambda key: f"{key} is a valid URL."
IS_NOT_URL_OR_EMPTY_ERROR_MESSAGE = lambda key: f"{key} is a valid URL or empty."


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
