from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from flunt.validations.strings_validation_contract import (
    StringValidationContract,
)

if TYPE_CHECKING:
    from tests.mocks.entity.sample_entity import SampleEntity


@pytest.fixture
def key() -> str:
    return "first_name"


@pytest.fixture
def message() -> str:
    return "any message"


def test_should_be_valid_when_is_not_none_or_white_space(
    entity_mock: SampleEntity, key: str, message: str
) -> None:
    contract = StringValidationContract().is_not_none_or_white_space(
        entity_mock.first_name, key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_is_none(
    key: str, message: str
) -> None:
    contract = StringValidationContract().is_not_none_or_white_space(
        None,
        key,
        message,
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_invalid_and_return_once_notification_when_white_space(
    key: str, message: str
) -> None:
    contract = StringValidationContract().is_not_none_or_white_space(
        " ", key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_and_not_return_notification_when_contains_a_search_string(
    entity_mock: SampleEntity, key: str, message: str
) -> None:
    contract = StringValidationContract().contains(
        entity_mock.full_name, entity_mock.last_name, key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_contains_a_search_string(
    entity_mock: SampleEntity, key: str, message: str
) -> None:
    contract = StringValidationContract().contains(
        entity_mock.full_name, "Vitor", key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_and_not_return_notification_when_not_contains_a_search_string(
    entity_mock: SampleEntity, key: str, message: str
) -> None:
    contract = StringValidationContract().not_contains(
        entity_mock.full_name, "Vitor", key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_contains_a_search_string(
    entity_mock: SampleEntity, key: str, message: str
) -> None:
    contract = StringValidationContract().not_contains(
        entity_mock.full_name, entity_mock.last_name, key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1
