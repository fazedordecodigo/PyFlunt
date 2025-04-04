from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from flunt.validations.email_validation_contract import EmailValidationContract

if TYPE_CHECKING:
    from tests.mocks.entity.sample_entity import SampleEntity


@pytest.fixture
def message() -> str:
    return "Custom message here"


def test_should_be_valid_when_correct_email(
    entity_mock: SampleEntity, message: str
) -> None:
    contract = EmailValidationContract().is_email(
        entity_mock.email_valid, "email", message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_return_a_once_notification_when_email_is_invalid(
    entity_mock: SampleEntity, message: str
) -> None:
    contract = EmailValidationContract().is_email(
        entity_mock.email_invalid, "email", message
    )
    assert len(contract.get_notifications()) == 1
