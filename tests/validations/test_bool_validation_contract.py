import pytest
from flunt.validations.contract import Contract

@pytest.fixture()
def message():
    yield 'Custom message here'


def test_should_be_valid_when_is_true(entity_mock, message):
	contract = (
		Contract()
		.requires(entity_mock.bool_true_property, 'Bool', message)
		.is_true(entity_mock.bool_true_property, 'Bool', message)
	)
	assert contract.is_valid


def test_should_be_valid_when_is_false(entity_mock, message):
	contract = (
		Contract()
		.requires(entity_mock.bool_true_property, 'Bool', message)
		.is_false(entity_mock.bool_false_property, 'Bool', message)
	)
	assert contract.is_valid


def test_should_return_a_once_notification_when_is_true_is_invalid(entity_mock, message):
	contract = (
		Contract()
		.requires(entity_mock.bool_true_property, 'Bool', message)
		.is_true(entity_mock.bool_false_property, 'Bool', message)
	)
	assert len(contract.get_notifications()) == 1


def test_should_return_a_once_notification_when_is_false_is_invalid(
	entity_mock, message
):
	contract = (
		Contract()
		.requires(entity_mock.bool_true_property, 'Bool', message)
		.is_false(entity_mock.bool_true_property, 'Bool', message)
	)
	assert len(contract.get_notifications()) == 1


def test_should_return_valid_when_is_none_is_valid(entity_mock, message):
	contract = (
		Contract()
		.requires(entity_mock.bool_true_property, 'Bool', message)
		.is_none(entity_mock.bool_none_property, 'Bool', message)
	)
	assert contract.is_valid


def test_should_return_a_once_notification_when_is_none_is_invalid(entity_mock, message):
	contract = (
		Contract()
		.requires(entity_mock.bool_true_property, 'Bool', message)
		.is_none(entity_mock.bool_true_property, 'Bool', message)
	)
	assert len(contract.get_notifications()) == 1


def test_should_return_valid_when_is_not_none_is_valid(entity_mock, message):
	contract = (
		Contract()
		.requires(entity_mock.bool_true_property, 'Bool', message)
		.is_not_none(entity_mock.bool_true_property, 'Bool', message)
	)
	assert contract.is_valid


def test_should_return_a_once_notification_when_is_not_none_is_invalid(
	entity_mock, message
):
	contract = (
		Contract()
		.requires(entity_mock.bool_true_property, 'Bool', message)
		.is_not_none(entity_mock.bool_none_property, 'Bool', message)
	)
	assert len(contract.get_notifications()) == 1
