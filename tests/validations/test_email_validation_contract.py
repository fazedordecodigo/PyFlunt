import pytest
from flunt.validations.contract import Contract

@pytest.fixture()
def message():
    yield 'Custom message here'

def test_should_be_valid_when_correct_email(entity_mock, message):
	contract = (
		Contract()
		.requires(entity_mock.email_valid, 'Email', message)
		.is_email(entity_mock.email_valid, 'email', message)
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_return_a_once_notification_when_email_is_invalid(entity_mock, message):
	contract = (
		Contract()
		.requires(entity_mock.email_invalid, 'Email', message)
		.is_email(entity_mock.email_invalid, 'email', message)
	)
	assert len(contract.get_notifications()) == 1
