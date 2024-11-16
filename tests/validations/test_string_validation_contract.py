import pytest

from flunt.validations.strings_validation_contract import (
    StringValidationContract,
)
from tests.mocks.entity.sample_entity import SampleEntity


@pytest.fixture
def key():
    return "first_name"


@pytest.fixture
def message():
    return "any message"


def test_should_be_valid_when_is_not_none_or_white_space(
    entity_mock: SampleEntity, key, message
):
    contract = StringValidationContract().is_not_none_or_white_space(
        entity_mock.first_name, key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_is_none(
    key, message
):
    contract = StringValidationContract().is_not_none_or_white_space(
        None, key, message
    )  # type: ignore
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_invalid_and_return_once_notification_when_white_space(
    key, message
):
    contract = StringValidationContract().is_not_none_or_white_space(
        " ", key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_and_not_return_notification_when_contains_a_search_string(
    entity_mock: SampleEntity, key, message
):
    contract = StringValidationContract().contains(
        entity_mock.full_name, entity_mock.last_name, key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_contains_a_search_string(
    entity_mock: SampleEntity, key, message
):
    contract = StringValidationContract().contains(
        entity_mock.full_name, "Vitor", key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_and_not_return_notification_when_not_contains_a_search_string(
    entity_mock: SampleEntity, key, message
):
    contract = StringValidationContract().not_contains(
        entity_mock.full_name, "Vitor", key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_contains_a_search_string(
    entity_mock: SampleEntity, key, message
):
    contract = StringValidationContract().not_contains(
        entity_mock.full_name, entity_mock.last_name, key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1
