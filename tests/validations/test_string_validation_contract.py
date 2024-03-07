import pytest
from tests.mocks.entity.sample_entity import SampleEntity
from flunt.validations.strings_validation_contract import StringValidationContract


@pytest.fixture()
def key():
    yield 'first_name'


@pytest.fixture()
def message():
	yield 'any message'


def test_should_be_valid_when_is_lower_than_20(entity_mock: SampleEntity, key, message):
	contract = StringValidationContract().is_lower_than(
		entity_mock.first_name, 20, key, message
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_lower_than_5(
	entity_mock: SampleEntity, key, message
):
	contract = StringValidationContract().is_lower_than(
		entity_mock.first_name, 5, key, message
	)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_lower_or_equals_than_20(
	entity_mock: SampleEntity, key, message
):
	contract = StringValidationContract().is_lower_or_equals_than(
		entity_mock.first_name, 20, key, message
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_lower_or_equals_than_14(
	entity_mock: SampleEntity, key, message
):
	contract = StringValidationContract().is_lower_or_equals_than(
		entity_mock.first_name, 14, key, message
	)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_greater_than_10(entity_mock: SampleEntity, key, message):
	contract = StringValidationContract().is_greater_than(
		entity_mock.first_name, 10, key, message
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_greater_than_15(
	entity_mock: SampleEntity, key, message
):
	contract = StringValidationContract().is_greater_than(
		entity_mock.first_name, 15, key, message
	)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_greater_or_equals_than_13(
	entity_mock: SampleEntity, key, message
):
	contract = StringValidationContract().is_greater_or_equals_than(
		entity_mock.first_name, 13, key, message
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_greater_or_equals_than_14(
	entity_mock: SampleEntity, key, message
):
	contract = StringValidationContract().is_greater_or_equals_than(
		entity_mock.first_name, 14, key, message
	)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


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


def test_should_be_valid_and_not_return_notification_when_contains_a_search_string(entity_mock: SampleEntity, key, message):
	contract = StringValidationContract().contains(entity_mock.first_name, "any", key, message)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_contains_a_search_string(entity_mock: SampleEntity, key, message):
	contract = StringValidationContract().contains(entity_mock.first_name, "bla", key, message)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


def test_should_be_valid_and_not_return_notification_when_not_contains_a_search_string(entity_mock: SampleEntity, key, message):
	contract = StringValidationContract().not_contains(entity_mock.first_name, "bla", key, message)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_contains_a_search_string(entity_mock: SampleEntity, key, message):
	contract = StringValidationContract().not_contains(entity_mock.first_name, "any", key, message)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


def test_should_be_valid_and_not_return_notification_when_value_is_between():
	contract = StringValidationContract().is_between("any_text", 1, 10, "test", "any_message")
	assert contract.is_valid


def test_should_be_invalid_and_return_once_notification_when_value_is_not_between():
	contract = StringValidationContract().is_between("any_text", 10, 20, "test", "any_message")
	assert contract.is_valid is False
