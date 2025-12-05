from datetime import UTC, date, datetime
from unittest.mock import MagicMock, patch

import pytest

from flunt.validations.datetime_validation_contract import (
    DateTimeValidationContract,
)


@pytest.fixture
def contract() -> DateTimeValidationContract:
    return DateTimeValidationContract()


# --------------------------------------------------------------------------
# is_date_after
# --------------------------------------------------------------------------


def test_is_date_after_with_valid_date(
    contract: DateTimeValidationContract,
) -> None:
    value = date(2023, 1, 2)
    comparer = date(2023, 1, 1)
    contract.is_date_after(value, comparer, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


def test_is_date_after_with_equal_date(
    contract: DateTimeValidationContract,
) -> None:
    value = date(2023, 1, 1)
    comparer = date(2023, 1, 1)
    contract.is_date_after(value, comparer, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_after_with_invalid_date(
    contract: DateTimeValidationContract,
) -> None:
    value = date(2023, 1, 1)
    comparer = date(2023, 1, 2)
    contract.is_date_after(value, comparer, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_after_with_none(
    contract: DateTimeValidationContract,
) -> None:
    contract.is_date_after(None, date(2023, 1, 1), "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_after_mixed_types_are_normalized(
    contract: DateTimeValidationContract,
) -> None:
    value = date(2023, 1, 2)
    comparer = datetime(2023, 1, 1, 12, 0, 0, tzinfo=UTC)
    contract.is_date_after(value, comparer, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


def test_is_date_after_naive_and_aware_are_normalized(
    contract: DateTimeValidationContract,
) -> None:
    value = datetime(2023, 1, 2, 12, 0, 0, tzinfo=UTC)
    comparer = datetime(2023, 1, 3, 12, 0, 0, tzinfo=UTC).replace(tzinfo=None)
    contract.is_date_after(value, comparer, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


# --------------------------------------------------------------------------
# is_date_before
# --------------------------------------------------------------------------


def test_is_date_before_with_valid_date(
    contract: DateTimeValidationContract,
) -> None:
    value = date(2023, 1, 1)
    comparer = date(2023, 1, 2)
    contract.is_date_before(value, comparer, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


def test_is_date_before_with_equal_date(
    contract: DateTimeValidationContract,
) -> None:
    value = date(2023, 1, 1)
    comparer = date(2023, 1, 1)
    contract.is_date_before(value, comparer, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_before_with_invalid_date(
    contract: DateTimeValidationContract,
) -> None:
    value = date(2023, 1, 2)
    comparer = date(2023, 1, 1)
    contract.is_date_before(value, comparer, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_before_with_none(
    contract: DateTimeValidationContract,
) -> None:
    contract.is_date_before(None, date(2023, 1, 1), "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_before_mixed_types_are_normalized(
    contract: DateTimeValidationContract,
) -> None:
    value = date(2023, 1, 1)
    comparer = datetime(2023, 1, 2, 12, 0, 0, tzinfo=UTC)
    contract.is_date_before(value, comparer, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


# --------------------------------------------------------------------------
# is_date_between
# --------------------------------------------------------------------------


def test_is_date_between_with_valid_range(
    contract: DateTimeValidationContract,
) -> None:
    start = date(2023, 1, 1)
    end = date(2023, 1, 3)
    value = date(2023, 1, 2)
    contract.is_date_between(value, start, end, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


def test_is_date_between_with_start_boundary(
    contract: DateTimeValidationContract,
) -> None:
    start = date(2023, 1, 1)
    end = date(2023, 1, 3)
    value = date(2023, 1, 1)
    contract.is_date_between(value, start, end, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


def test_is_date_between_with_end_boundary(
    contract: DateTimeValidationContract,
) -> None:
    start = date(2023, 1, 1)
    end = date(2023, 1, 3)
    value = date(2023, 1, 3)
    contract.is_date_between(value, start, end, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


def test_is_date_between_with_invalid_lower(
    contract: DateTimeValidationContract,
) -> None:
    start = date(2023, 1, 2)
    end = date(2023, 1, 3)
    value = date(2023, 1, 1)
    contract.is_date_between(value, start, end, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_between_with_invalid_upper(
    contract: DateTimeValidationContract,
) -> None:
    start = date(2023, 1, 1)
    end = date(2023, 1, 2)
    value = date(2023, 1, 3)
    contract.is_date_between(value, start, end, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_between_with_none(
    contract: DateTimeValidationContract,
) -> None:
    start = date(2023, 1, 1)
    end = date(2023, 1, 3)
    contract.is_date_between(None, start, end, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_between_mixed_types_are_normalized(
    contract: DateTimeValidationContract,
) -> None:
    start = date(2023, 1, 1)
    end = datetime(2023, 1, 3, 12, 0, 0, tzinfo=UTC)
    value = datetime(2023, 1, 2, 12, 0, 0, tzinfo=UTC)
    contract.is_date_between(value, start, end, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


# --------------------------------------------------------------------------
# is_date_in_past
# --------------------------------------------------------------------------


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_date_in_past_with_past_date(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    mock_get_today.return_value = date(2023, 1, 2)
    value = date(2023, 1, 1)
    contract.is_date_in_past(value, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_date_in_past_with_today(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    mock_get_today.return_value = date(2023, 1, 1)
    value = date(2023, 1, 1)
    contract.is_date_in_past(value, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_date_in_past_with_future_date(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    mock_get_today.return_value = date(2023, 1, 1)
    value = date(2023, 1, 2)
    contract.is_date_in_past(value, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_in_past_with_none(
    contract: DateTimeValidationContract,
) -> None:
    contract.is_date_in_past(None, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_date_in_past_with_datetime(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    # Should handle datetime by extracting date()
    mock_get_today.return_value = date(2023, 1, 2)
    value = datetime(2023, 1, 1, 12, 0, 0, tzinfo=UTC)
    contract.is_date_in_past(value, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


# --------------------------------------------------------------------------
# is_date_in_future
# --------------------------------------------------------------------------


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_date_in_future_with_future_date(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    mock_get_today.return_value = date(2023, 1, 1)
    value = date(2023, 1, 2)
    contract.is_date_in_future(value, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_date_in_future_with_today(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    mock_get_today.return_value = date(2023, 1, 1)
    value = date(2023, 1, 1)
    contract.is_date_in_future(value, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_date_in_future_with_past_date(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    mock_get_today.return_value = date(2023, 1, 2)
    value = date(2023, 1, 1)
    contract.is_date_in_future(value, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_date_in_future_with_none(
    contract: DateTimeValidationContract,
) -> None:
    contract.is_date_in_future(None, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_date_in_future_with_datetime(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    # Should handle datetime by extracting date()
    mock_get_today.return_value = date(2023, 1, 1)
    value = datetime(2023, 1, 2, 12, 0, 0, tzinfo=UTC)
    contract.is_date_in_future(value, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


# --------------------------------------------------------------------------
# is_today
# --------------------------------------------------------------------------


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_today_with_today(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    mock_get_today.return_value = date(2023, 1, 1)
    value = date(2023, 1, 1)
    contract.is_today(value, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_today_with_not_today(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    mock_get_today.return_value = date(2023, 1, 1)
    value = date(2023, 1, 2)
    contract.is_today(value, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


def test_is_today_with_none(
    contract: DateTimeValidationContract,
) -> None:
    contract.is_today(None, "field", "message")
    assert contract.is_valid is False
    assert len(contract.notifications) == 1


@patch("flunt.validations.datetime_validation_contract._get_today")
def test_is_today_with_datetime(
    mock_get_today: MagicMock, contract: DateTimeValidationContract
) -> None:
    # Should handle datetime by extracting date()
    mock_get_today.return_value = date(2023, 1, 1)
    value = datetime(2023, 1, 1, 12, 0, 0, tzinfo=UTC)
    contract.is_today(value, "field", "message")
    assert contract.is_valid
    assert len(contract.notifications) == 0
