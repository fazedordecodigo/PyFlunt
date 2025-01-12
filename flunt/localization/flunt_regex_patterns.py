"""Module Flunt Regex Patterns."""

REGEX_PATTERNS = {
    "email": r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
    "passport": r"^(?!^0+$)[a-zA-Z0-9]{3,20}$",
    "only_numbers": r"^\d+$",
    "only_letters_and_numbers": r"[A-Za-z0-9_-]",
    "url": r"^(http|https):(\/\/www\.|\/\/www\.|\/\/|\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"
           r"|(http|https):(\/\/localhost:\d*|\/\/127\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]"
           r"|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))(:[0-9]{1,5})?(\/.*)?$",
    "cpf": r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$",
    "cnpj": r"^\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}$",
}

def get_pattern(name: str) -> str | None:
    """Retrieve a regex pattern by its name."""
    return REGEX_PATTERNS.get(name)