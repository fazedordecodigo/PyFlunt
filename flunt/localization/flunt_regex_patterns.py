"""Module Flunt Regex Patterns."""

REGEX_EMAIL = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
REGEX_CPF_CNPJ = r"""
([0-9]{2}[\.]?[0-9]{3}[\.]?
[0-9]{3}[\/]?[0-9]{4}[-]?
[0-9]{2})|([0-9]{3}[\.]?
[0-9]{3}[\.]?
[0-9]{3}[-]?
[0-9]{2})
"""


class FluntRegexPatterns():
    """Class Notifiable."""

    def __init__(self) -> None:
        """Found 'Constructor'."""
        self.cpf_cnpj_regex_pattern = REGEX_CPF_CNPJ
        self.email_regex_pattern = REGEX_EMAIL
