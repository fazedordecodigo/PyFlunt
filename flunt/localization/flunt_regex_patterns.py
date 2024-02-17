"""Module Flunt Regex Patterns."""

REGEX_EMAIL = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
REGEX_PASSPORT = r'^(?!^0+$)[a-zA-Z0-9]{3,20}$'
REGEX_ONLY_NUMBERS = r'^\d+$'
REGEX_ONLY_LETTERS_AND_NUMBERS = r'[A-Za-z0-9_-]'
REGEX_URL = r'^(http|https):(\/\/www\.|\/\/www\.|\/\/|\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$|(http|https):(\/\/localhost:\d*|\/\/127\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:[0-9]{1,5})?(\/.*)?$'
REGEX_CPF = r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$'
REGEX_CNPJ = r'^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$'


class FluntRegexPatterns:
	"""
	FluntRegexPatterns.

	This class encapsulates commonly used regular expression patterns.
	It provides attributes to access the regular expression patterns
	related to CPF, CNPJ, email, URL, only numbers, only letters and numbers,
	and passport.

	Attributes:
	----------
	- cpf_regex_pattern: str
	    The regular expression pattern for CPF.
	- cnpj_regex_pattern: str
	    The regular expression pattern for CNPJ.
	- email_regex_pattern: str
	    The regular expression pattern for email.
	- url_regex_pattern: str
	    The regular expression pattern for URL.
	- only_number_regex_pattern: str
	    The regular expression pattern for only numbers.
	- only_letters_and_numbers_regex_pattern: str
	    The regular expression pattern for only letters and numbers.
	- passport_regex_pattern: str
	    The regular expression pattern for passport.
	TODO: Alterar de classe para outra estrutura de dados.
	"""

	def __init__(self) -> None:
		"""Initialize a new instance of the FluntRegexPatterns class."""
		self.cpf_regex_pattern = REGEX_CPF
		self.cnpj_regex_pattern = REGEX_CNPJ
		self.email_regex_pattern = REGEX_EMAIL
		self.url_regex_pattern = REGEX_URL
		self.only_number_regex_pattern = REGEX_ONLY_NUMBERS
		self.only_letters_and_numbers_regex_pattern = REGEX_ONLY_LETTERS_AND_NUMBERS
		self.passport_regex_pattern = REGEX_PASSPORT
