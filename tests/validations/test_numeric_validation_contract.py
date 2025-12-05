"""Tests for Numeric Validation Contract."""

from __future__ import annotations

from flunt.validations.contract import Contract

# Test constants
EXPECTED_THREE_NOTIFICATIONS = 3


class TestIsGreaterThanNumber:
    """Tests for is_greater_than_number validation."""

    def test_should_be_valid_when_value_is_greater(self) -> None:
        """Test valid when value is greater than comparer."""
        contract = Contract().is_greater_than_number(25, 18, "idade")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_invalid_when_value_is_equal(self) -> None:
        """Test invalid when value equals comparer."""
        contract = Contract().is_greater_than_number(18, 18, "idade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1

    def test_should_be_invalid_when_value_is_lower(self) -> None:
        """Test invalid when value is lower than comparer."""
        contract = Contract().is_greater_than_number(15, 18, "idade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1

    def test_should_be_invalid_when_value_is_none(self) -> None:
        """Test invalid when value is None."""
        contract = Contract().is_greater_than_number(None, 18, "idade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1

    def test_should_work_with_floats(self) -> None:
        """Test that it works with float numbers."""
        contract = Contract().is_greater_than_number(3.5, 3.0, "valor")
        assert contract.is_valid


class TestIsGreaterOrEqualsThanNumber:
    """Tests for is_greater_or_equals_than_number validation."""

    def test_should_be_valid_when_value_is_greater(self) -> None:
        """Test valid when value is greater."""
        contract = Contract().is_greater_or_equals_than_number(25, 18, "idade")
        assert contract.is_valid

    def test_should_be_valid_when_value_is_equal(self) -> None:
        """Test valid when value equals comparer."""
        contract = Contract().is_greater_or_equals_than_number(18, 18, "idade")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_invalid_when_value_is_lower(self) -> None:
        """Test invalid when value is lower."""
        contract = Contract().is_greater_or_equals_than_number(17, 18, "idade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1


class TestIsLowerThanNumber:
    """Tests for is_lower_than_number validation."""

    def test_should_be_valid_when_value_is_lower(self) -> None:
        """Test valid when value is lower."""
        contract = Contract().is_lower_than_number(15, 18, "idade")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_invalid_when_value_is_equal(self) -> None:
        """Test invalid when value equals comparer."""
        contract = Contract().is_lower_than_number(18, 18, "idade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1

    def test_should_be_invalid_when_value_is_greater(self) -> None:
        """Test invalid when value is greater."""
        contract = Contract().is_lower_than_number(25, 18, "idade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1


class TestIsLowerOrEqualsThanNumber:
    """Tests for is_lower_or_equals_than_number validation."""

    def test_should_be_valid_when_value_is_lower(self) -> None:
        """Test valid when value is lower."""
        contract = Contract().is_lower_or_equals_than_number(15, 18, "idade")
        assert contract.is_valid

    def test_should_be_valid_when_value_is_equal(self) -> None:
        """Test valid when value equals comparer."""
        contract = Contract().is_lower_or_equals_than_number(18, 18, "idade")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_invalid_when_value_is_greater(self) -> None:
        """Test invalid when value is greater."""
        contract = Contract().is_lower_or_equals_than_number(25, 18, "idade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1


class TestIsBetweenNumbers:
    """Tests for is_between_numbers validation."""

    def test_should_be_valid_when_value_is_in_range(self) -> None:
        """Test valid when value is in range."""
        contract = Contract().is_between_numbers(25, 18, 65, "idade")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_valid_when_value_equals_min(self) -> None:
        """Test valid when value equals minimum."""
        contract = Contract().is_between_numbers(18, 18, 65, "idade")
        assert contract.is_valid

    def test_should_be_valid_when_value_equals_max(self) -> None:
        """Test valid when value equals maximum."""
        contract = Contract().is_between_numbers(65, 18, 65, "idade")
        assert contract.is_valid

    def test_should_be_invalid_when_value_is_below_min(self) -> None:
        """Test invalid when value is below minimum."""
        contract = Contract().is_between_numbers(17, 18, 65, "idade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1

    def test_should_be_invalid_when_value_is_above_max(self) -> None:
        """Test invalid when value is above maximum."""
        contract = Contract().is_between_numbers(70, 18, 65, "idade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1


class TestIsPositive:
    """Tests for is_positive validation."""

    def test_should_be_valid_when_value_is_positive(self) -> None:
        """Test valid when value is positive."""
        contract = Contract().is_positive(10, "quantidade")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_invalid_when_value_is_zero(self) -> None:
        """Test invalid when value is zero."""
        contract = Contract().is_positive(0, "quantidade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1

    def test_should_be_invalid_when_value_is_negative(self) -> None:
        """Test invalid when value is negative."""
        contract = Contract().is_positive(-5, "quantidade")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1

    def test_should_work_with_floats(self) -> None:
        """Test that it works with float numbers."""
        contract = Contract().is_positive(0.1, "valor")
        assert contract.is_valid


class TestIsNegative:
    """Tests for is_negative validation."""

    def test_should_be_valid_when_value_is_negative(self) -> None:
        """Test valid when value is negative."""
        contract = Contract().is_negative(-10, "saldo")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_invalid_when_value_is_zero(self) -> None:
        """Test invalid when value is zero."""
        contract = Contract().is_negative(0, "saldo")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1

    def test_should_be_invalid_when_value_is_positive(self) -> None:
        """Test invalid when value is positive."""
        contract = Contract().is_negative(5, "saldo")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1


class TestIsZero:
    """Tests for is_zero validation."""

    def test_should_be_valid_when_value_is_zero(self) -> None:
        """Test valid when value is zero."""
        contract = Contract().is_zero(0, "contador")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_invalid_when_value_is_positive(self) -> None:
        """Test invalid when value is positive."""
        contract = Contract().is_zero(5, "contador")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1

    def test_should_be_invalid_when_value_is_negative(self) -> None:
        """Test invalid when value is negative."""
        contract = Contract().is_zero(-5, "contador")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1


class TestIsNotZero:
    """Tests for is_not_zero validation."""

    def test_should_be_valid_when_value_is_positive(self) -> None:
        """Test valid when value is positive."""
        contract = Contract().is_not_zero(5, "divisor")
        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_should_be_valid_when_value_is_negative(self) -> None:
        """Test valid when value is negative."""
        contract = Contract().is_not_zero(-5, "divisor")
        assert contract.is_valid

    def test_should_be_invalid_when_value_is_zero(self) -> None:
        """Test invalid when value is zero."""
        contract = Contract().is_not_zero(0, "divisor")
        assert not contract.is_valid
        assert len(contract.get_notifications()) == 1


class TestNumericValidationContract:
    """Integration tests for NumericValidationContract."""

    def test_contract_has_numeric_methods(self) -> None:
        """Test that Contract has numeric validation methods."""
        contract = Contract()
        assert hasattr(contract, "is_greater_than_number")
        assert hasattr(contract, "is_greater_or_equals_than_number")
        assert hasattr(contract, "is_lower_than_number")
        assert hasattr(contract, "is_lower_or_equals_than_number")
        assert hasattr(contract, "is_between_numbers")
        assert hasattr(contract, "is_positive")
        assert hasattr(contract, "is_negative")
        assert hasattr(contract, "is_zero")
        assert hasattr(contract, "is_not_zero")

    def test_multiple_numeric_validations_in_chain(self) -> None:
        """Test multiple numeric validations in chain."""
        contract = (
            Contract()
            .is_positive(100, "preco", "Preço deve ser positivo")
            .is_greater_or_equals_than_number(
                18, 18, "idade", "Deve ser maior de idade"
            )
            .is_between_numbers(
                25, 0, 100, "desconto", "Desconto deve estar entre 0 e 100"
            )
        )

        assert contract.is_valid
        assert len(contract.get_notifications()) == 0

    def test_numeric_validations_with_errors(self) -> None:
        """Test numeric validations with errors."""
        contract = (
            Contract()
            .is_positive(-10, "preco", "Preço deve ser positivo")
            .is_greater_or_equals_than_number(
                16, 18, "idade", "Deve ser maior de idade"
            )
            .is_between_numbers(150, 0, 100, "desconto", "Desconto inválido")
        )

        assert not contract.is_valid
        assert (
            len(contract.get_notifications()) == EXPECTED_THREE_NOTIFICATIONS
        )

    def test_mixed_validations(self) -> None:
        """Test mixing numeric validations with other validations."""
        contract = (
            Contract()
            .requires("João", "nome", "Nome obrigatório")
            .is_email("joao@email.com", "email", "Email inválido")
            .is_greater_or_equals_than_number(
                25, 18, "idade", "Deve ser maior de idade"
            )
            .is_positive(1000.50, "saldo", "Saldo deve ser positivo")
        )

        assert contract.is_valid
        assert len(contract.get_notifications()) == 0
