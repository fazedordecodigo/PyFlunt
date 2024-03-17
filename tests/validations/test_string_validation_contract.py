import pytest
from tests.mocks.entity.sample_entity import SampleEntity
from flunt.validations.strings_validation_contract import StringValidationContract


@pytest.fixture()
def key():
    yield 'first_name'


@pytest.fixture()
def message():
	yield 'any message'


def test_should_be_valid_when_is_not_none_or_white_space(
	entity_mock: SampleEntity, key, message
):
	contract = StringValidationContract().is_not_none_or_white_space(
		entity_mock.first_name, key, message
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_is_none(key, message):
	contract = StringValidationContract().is_not_none_or_white_space(None, key, message)  # type: ignore
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


def test_should_be_invalid_and_return_once_notification_when_white_space(key, message):
	contract = StringValidationContract().is_not_none_or_white_space(' ', key, message)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1
