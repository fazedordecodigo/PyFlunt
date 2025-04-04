from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from flunt.constants.messages import IS_FALSE, IS_TRUE
from flunt.validations.bool_validation_contract import BoolValidationContract

if TYPE_CHECKING:
    from tests.mocks.entity.sample_entity import SampleEntity


@pytest.fixture
def message() -> str:
    return "Custom message here"


def test_should_be_valid_when_is_true(
    entity_mock: SampleEntity, message: str
) -> None:
    contract = BoolValidationContract().is_true(
        entity_mock.bool_true_property, "Bool", message
    )
    assert contract.is_valid


def test_should_be_valid_when_is_false(
    entity_mock: SampleEntity, message: str
) -> None:
    contract = BoolValidationContract().is_false(
        entity_mock.bool_false_property, "Bool", message
    )
    assert contract.is_valid


def test_should_return_a_once_notification_when_is_true_is_invalid(
    entity_mock: SampleEntity, message: str
) -> None:
    contract = BoolValidationContract().is_true(
        entity_mock.bool_false_property, "Bool", message
    )
    assert len(contract.get_notifications()) == 1


def test_should_return_a_once_notification_when_is_false_is_invalid(
    entity_mock: SampleEntity, message: str
) -> None:
    contract = BoolValidationContract().is_false(
        entity_mock.bool_true_property, "Bool", message
    )
    assert len(contract.get_notifications()) == 1


def test_should_return_a_standard_message_when_is_true_is_invalid(
    entity_mock: SampleEntity,
) -> None:
    contract = BoolValidationContract().is_true(
        entity_mock.bool_false_property, "Bool"
    )
    assert contract.get_notifications()[0].message == IS_TRUE.format("Bool")


def test_should_return_a_standard_message_when_is_false_is_invalid(
    entity_mock: SampleEntity,
) -> None:
    contract = BoolValidationContract().is_false(
        entity_mock.bool_true_property, "Bool"
    )
    assert contract.get_notifications()[0].message == IS_FALSE.format("Bool")


def test_should_return_a_custom_message_when_is_true_is_invalid(
    entity_mock: SampleEntity, message: str
) -> None:
    contract = BoolValidationContract().is_true(
        entity_mock.bool_false_property, "Bool", message
    )
    assert contract.get_notifications()[0].message == message


def test_should_return_a_custom_message_when_is_false_is_invalid(
    entity_mock: SampleEntity, message: str
) -> None:
    contract = BoolValidationContract().is_false(
        entity_mock.bool_true_property, "Bool", message
    )
    assert contract.get_notifications()[0].message == message
