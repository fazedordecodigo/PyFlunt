"""Module Brazilian Document Validation Contract."""

from __future__ import annotations

from typing import Self

from flunt.constants.messages import IS_NOT_CNPJ, IS_NOT_CPF
from flunt.notifications.notifiable import Notifiable

# Brazilian document constants
CPF_LENGTH = 11
CNPJ_LENGTH = 14
MAX_CHECKSUM_DIGIT = 10


def _only_digits(value: str | None) -> str:
    """
    Remove all non-digit characters from a string.

    Args:
        value: The string to clean

    Returns:
        String containing only digits

    """
    if not isinstance(value, str):
        return ""
    return "".join(filter(str.isdigit, value))


def _validate_cpf(cpf: str | None) -> bool:
    """
    Validate a CPF (Cadastro de Pessoa Física) with check digits.

    Args:
        cpf: The CPF to validate (with or without formatting)

    Returns:
        True if valid, False otherwise

    Examples:
        >>> _validate_cpf("123.456.789-09")
        True
        >>> _validate_cpf("12345678909")
        True
        >>> _validate_cpf("111.111.111-11")
        False
        >>> _validate_cpf("000.000.000-00")
        False

    """
    if not cpf:
        return False

    # Remove formatting
    cpf_clean = _only_digits(cpf)

    # CPF must have exactly 11 digits
    if len(cpf_clean) != CPF_LENGTH:
        return False

    # Reject known invalid CPFs (all same digits)
    if cpf_clean in {
        "00000000000",
        "11111111111",
        "22222222222",
        "33333333333",
        "44444444444",
        "55555555555",
        "66666666666",
        "77777777777",
        "88888888888",
        "99999999999",
    }:
        return False

    # Validate first check digit
    sum_first = sum(int(cpf_clean[i]) * (10 - i) for i in range(9))
    first_digit = (sum_first * 10 % 11) % 10

    if int(cpf_clean[9]) != first_digit:
        return False

    # Validate second check digit
    sum_second = sum(int(cpf_clean[i]) * (11 - i) for i in range(10))
    second_digit = (sum_second * 10 % 11) % 10

    if int(cpf_clean[10]) != second_digit:
        return False

    return True


def _validate_cnpj(cnpj: str | None) -> bool:
    """
    Validate a CNPJ (Cadastro Nacional de Pessoa Jurídica) with check digits.

    Args:
        cnpj: The CNPJ to validate (with or without formatting)

    Returns:
        True if valid, False otherwise

    Examples:
        >>> _validate_cnpj("11.222.333/0001-81")
        True
        >>> _validate_cnpj("11222333000181")
        True
        >>> _validate_cnpj("11.111.111/1111-11")
        False
        >>> _validate_cnpj("00.000.000/0000-00")
        False

    """
    if not cnpj:
        return False

    # Remove formatting
    cnpj_clean = _only_digits(cnpj)

    # CNPJ must have exactly 14 digits
    if len(cnpj_clean) != CNPJ_LENGTH:
        return False

    # Reject known invalid CNPJs (all same digits)
    if cnpj_clean in {
        "00000000000000",
        "11111111111111",
        "22222222222222",
        "33333333333333",
        "44444444444444",
        "55555555555555",
        "66666666666666",
        "77777777777777",
        "88888888888888",
        "99999999999999",
    }:
        return False

    # Validate first check digit
    weights_first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_first = sum(int(cnpj_clean[i]) * weights_first[i] for i in range(12))
    first_digit = 11 - (sum_first % 11)
    first_digit = 0 if first_digit >= MAX_CHECKSUM_DIGIT else first_digit

    if int(cnpj_clean[12]) != first_digit:
        return False

    # Validate second check digit
    weights_second = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_second = sum(int(cnpj_clean[i]) * weights_second[i] for i in range(13))
    second_digit = 11 - (sum_second % 11)
    second_digit = 0 if second_digit >= MAX_CHECKSUM_DIGIT else second_digit

    if int(cnpj_clean[13]) != second_digit:
        return False

    return True


class BrazilianDocumentValidationContract(Notifiable):
    """
    Contract for validating Brazilian documents.

    This class provides methods for validating CPF and CNPJ with complete
    check digit validation.

    """

    def is_cpf(
        self, value: str | None, field: str, message: str = IS_NOT_CPF
    ) -> Self:
        """
        Validate if a string is a valid CPF (Cadastro de Pessoa Física).

        This method validates both the format and the check digits of a CPF.
        It accepts CPF with or without formatting (dots and hyphens).

        Args:
            value: The CPF to validate (with or without formatting)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = BrazilianDocumentValidationContract()
            >>> contract.is_cpf("123.456.789-09", "cpf")
            >>> contract.is_valid  # True
            >>> contract.is_cpf("111.111.111-11", "cpf")
            >>> contract.is_valid  # False (sequential)
            >>> contract.is_cpf("123.456.789-00", "cpf")
            >>> contract.is_valid  # False (invalid check digit)

        """
        if not _validate_cpf(value):
            if message is IS_NOT_CPF:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self

    def is_cnpj(
        self, value: str | None, field: str, message: str = IS_NOT_CNPJ
    ) -> Self:
        """
        Validate if a string is a valid CNPJ (Cadastro Nacional de Pessoa Jurídica).

        This method validates both the format and the check digits of a CNPJ.
        It accepts CNPJ with or without formatting (dots, slash and hyphens).

        Args:
            value: The CNPJ to validate (with or without formatting)
            field: Field identifier for the notification
            message: Optional custom message

        Returns:
            Self for method chaining

        Examples:
            >>> contract = BrazilianDocumentValidationContract()
            >>> contract.is_cnpj("11.222.333/0001-81", "cnpj")
            >>> contract.is_valid  # True
            >>> contract.is_cnpj("11.111.111/1111-11", "cnpj")
            >>> contract.is_valid  # False (sequential)
            >>> contract.is_cnpj("11.222.333/0001-00", "cnpj")
            >>> contract.is_valid  # False (invalid check digit)

        """
        if not _validate_cnpj(value):
            if message is IS_NOT_CNPJ:
                self.add_notification(field, message.format(field))
                return self
            self.add_notification(field, message)
        return self
