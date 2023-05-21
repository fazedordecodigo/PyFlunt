
from flunt.validations.contract import Contract
from tests.mocks.value_objects.vo import Email


def test_should_be_valid_when_correct_email(entityMock):
    contract = (
        Contract()
        .requires(entityMock.email_valid, "Email")
        .is_email(entityMock.email_valid, "email", "any message")
    )
    assert contract.is_valid()
    assert len(contract.get_notifications()) == 0


def test_should_return_a_once_notification_when_email_is_invalid(entityMock):
    contract = (
        Contract()
        .requires(entityMock.email_invalid, "Email")
        .is_email(entityMock.email_invalid, "email", "any message")
    )
    assert len(contract.get_notifications()) == 1
