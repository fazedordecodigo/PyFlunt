"""Tests for Brazilian Document Validation Contract."""

from __future__ import annotations

from typing import ClassVar

import pytest

from flunt.validations.contract import Contract

# Test constants
EXPECTED_TWO_NOTIFICATIONS = 2


class TestCPFValidation:
    """Tests for CPF validation."""

    # Valid CPFs (real format with valid check digits)
    VALID_CPFS: ClassVar[list[str]] = [
        "123.456.789-09",  # Formatted
        "12345678909",  # Unformatted
        "111.444.777-35",  # Another valid
        "11144477735",  # Unformatted
    ]

    # Invalid CPFs
    INVALID_CPFS: ClassVar[list[str | None]] = [
        "111.111.111-11",  # Sequential (all same digits)
        "000.000.000-00",  # All zeros
        "999.999.999-99",  # All nines
        "123.456.789-00",  # Invalid check digit
        "123.456.789-10",  # Invalid check digit
        "12345678900",  # Invalid check digit (unformatted)
        "123.456.78",  # Too short
        "123.456.789-0",  # Too short
        "abc.def.ghi-jk",  # Non-numeric
        "",  # Empty
        None,  # None
    ]

    def test_should_be_valid_when_cpf_is_valid_formatted(self) -> None:
        """Test valid CPF with formatting."""
        contract = Contract().is_cpf("123.456.789-09", "cpf")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_valid_when_cpf_is_valid_unformatted(self) -> None:
        """Test valid CPF without formatting."""
        contract = Contract().is_cpf("12345678909", "cpf")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    @pytest.mark.parametrize("cpf", VALID_CPFS)
    def test_all_valid_cpfs(self, cpf: str) -> None:
        """Test all valid CPFs."""
        contract = Contract().is_cpf(cpf, "cpf")
        assert contract.is_valid, f"CPF {cpf} should be valid"

    @pytest.mark.parametrize("cpf", INVALID_CPFS)
    def test_all_invalid_cpfs(self, cpf: str | None) -> None:
        """Test all invalid CPFs."""
        contract = Contract().is_cpf(cpf, "cpf")
        assert not contract.is_valid, f"CPF {cpf} should be invalid"
        assert len(contract.get_notifications()) == 1

    def test_should_return_custom_message_when_cpf_invalid(self) -> None:
        """Test custom error message."""
        custom_message = "CPF inválido"
        contract = Contract().is_cpf("111.111.111-11", "cpf", custom_message)

        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1
        assert contract.get_notifications()[0].message == custom_message

    def test_should_return_default_message_when_cpf_invalid(self) -> None:
        """Test default error message."""
        contract = Contract().is_cpf("111.111.111-11", "cpf")

        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1
        assert "cpf" in contract.get_notifications()[0].message.lower()

    def test_cpf_validation_in_chain(self) -> None:
        """Test CPF validation in method chain."""
        contract = (
            Contract()
            .requires("João", "nome", "Nome obrigatório")
            .is_cpf("123.456.789-09", "cpf", "CPF inválido")
        )

        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_cpf_validation_in_chain_with_error(self) -> None:
        """Test CPF validation in chain with error."""
        contract = (
            Contract()
            .requires("", "nome", "Nome obrigatório")
            .is_cpf("111.111.111-11", "cpf", "CPF inválido")
        )

        assert not contract.is_valid
        assert len(contract.get_notifications()) == EXPECTED_TWO_NOTIFICATIONS


class TestCNPJValidation:
    """Tests for CNPJ validation."""

    # Valid CNPJs (real format with valid check digits)
    VALID_CNPJS: ClassVar[list[str]] = [
        "11.222.333/0001-81",  # Formatted
        "11222333000181",  # Unformatted
        "11.444.777/0001-61",  # Another valid
        "11444777000161",  # Unformatted
    ]

    # Invalid CNPJs
    INVALID_CNPJS: ClassVar[list[str | None]] = [
        "11.111.111/1111-11",  # Sequential
        "00.000.000/0000-00",  # All zeros
        "99.999.999/9999-99",  # All nines
        "11.222.333/0001-00",  # Invalid check digit
        "11.222.333/0001-82",  # Invalid check digit
        "11222333000100",  # Invalid check digit (unformatted)
        "11.222.333/0001",  # Too short
        "11.222.333",  # Too short
        "ab.cde.fgh/ijkl-mn",  # Non-numeric
        "",  # Empty
        None,  # None
    ]

    def test_should_be_valid_when_cnpj_is_valid_formatted(self) -> None:
        """Test valid CNPJ with formatting."""
        contract = Contract().is_cnpj("11.222.333/0001-81", "cnpj")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_valid_when_cnpj_is_valid_unformatted(self) -> None:
        """Test valid CNPJ without formatting."""
        contract = Contract().is_cnpj("11222333000181", "cnpj")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    @pytest.mark.parametrize("cnpj", VALID_CNPJS)
    def test_all_valid_cnpjs(self, cnpj: str) -> None:
        """Test all valid CNPJs."""
        contract = Contract().is_cnpj(cnpj, "cnpj")
        assert contract.is_valid, f"CNPJ {cnpj} should be valid"

    @pytest.mark.parametrize("cnpj", INVALID_CNPJS)
    def test_all_invalid_cnpjs(self, cnpj: str | None) -> None:
        """Test all invalid CNPJs."""
        contract = Contract().is_cnpj(cnpj, "cnpj")
        assert not contract.is_valid, f"CNPJ {cnpj} should be invalid"
        assert len(contract.get_notifications()) == 1

    def test_should_return_custom_message_when_cnpj_invalid(self) -> None:
        """Test custom error message."""
        custom_message = "CNPJ inválido"
        contract = Contract().is_cnpj(
            "11.111.111/1111-11", "cnpj", custom_message
        )

        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1
        assert contract.get_notifications()[0].message == custom_message

    def test_should_return_default_message_when_cnpj_invalid(self) -> None:
        """Test default error message."""
        contract = Contract().is_cnpj("11.111.111/1111-11", "cnpj")

        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1
        assert "cnpj" in contract.get_notifications()[0].message.lower()

    def test_cnpj_validation_in_chain(self) -> None:
        """Test CNPJ validation in method chain."""
        contract = (
            Contract()
            .requires("Empresa XYZ", "nome", "Nome obrigatório")
            .is_cnpj("11.222.333/0001-81", "cnpj", "CNPJ inválido")
        )

        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_cnpj_validation_in_chain_with_error(self) -> None:
        """Test CNPJ validation in chain with error."""
        contract = (
            Contract()
            .requires("", "nome", "Nome obrigatório")
            .is_cnpj("11.111.111/1111-11", "cnpj", "CNPJ inválido")
        )

        assert not contract.is_valid
        assert len(contract.get_notifications()) == EXPECTED_TWO_NOTIFICATIONS


class TestBrazilianDocumentValidationContract:
    """Integration tests for BrazilianDocumentValidationContract."""

    def test_contract_instance(self) -> None:
        """Test that Contract has Brazilian document methods."""
        contract = Contract()
        assert hasattr(contract, "is_cpf")
        assert hasattr(contract, "is_cnpj")

    def test_cpf_and_cnpj_together(self) -> None:
        """Test CPF and CNPJ validation together."""
        contract = (
            Contract()
            .is_cpf("123.456.789-09", "cpf", "CPF inválido")
            .is_cnpj("11.222.333/0001-81", "cnpj", "CNPJ inválido")
        )

        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_cpf_and_cnpj_both_invalid(self) -> None:
        """Test CPF and CNPJ both invalid."""
        contract = (
            Contract()
            .is_cpf("111.111.111-11", "cpf", "CPF inválido")
            .is_cnpj("11.111.111/1111-11", "cnpj", "CNPJ inválido")
        )

        assert not contract.is_valid
        assert len(contract.get_notifications()) == EXPECTED_TWO_NOTIFICATIONS
