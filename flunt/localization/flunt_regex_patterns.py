"""Module Flunt Regex Patterns."""

REGEX_EMAIL = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
REGEX_PASSPORT = "^(?!^0+$)[a-zA-Z0-9]{3,20}$"
REGEX_ONLY_NUMBERS = r"[^0-9]+"
REGEX_ONLY_LETTERS_AND_NUMBERS = r"[A-Za-z0-9_-]"
REGEX_URL = r"""
^(http|https):(\/\/www\.|\/\/www\.|\/\/|\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.
[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?
$|(http|https):(\/\/localhost:\d*|\/\/127\.
([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.
([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.
([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:[0-9]{1,5})?(\/.*)?$
"""

REGEX_CPF_CNPJ = r"""
([0-9]{2}[\.]?[0-9]{3}[\.]?
[0-9]{3}[\/]?[0-9]{4}[-]?
[0-9]{2})|([0-9]{3}[\.]?
[0-9]{3}[\.]?
[0-9]{3}[-]?
[0-9]{2})
"""


class FluntRegexPatterns:
    """Class FluntRegexPatterns."""

    def __init__(self) -> None:
        self.cpf_cnpj_regex_pattern = REGEX_CPF_CNPJ
        self.email_regex_pattern = REGEX_EMAIL
        self.url_regex_pattern = REGEX_URL
        self.only_number_regex_pattern = REGEX_ONLY_NUMBERS
        self.only_letters_and_numbers_regex_pattern = REGEX_ONLY_LETTERS_AND_NUMBERS
        self.passport_regex_pattern = REGEX_PASSPORT

