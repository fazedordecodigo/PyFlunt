from flunt.validations.contract import Contract

message = "Custom message here"


def test_should_be_valid_when_correct_email(entityMock):
    contract = (
        Contract()
        .requires(entityMock.email_valid, "Email", message)
        .is_email(entityMock.email_valid, "email", message)
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_return_a_once_notification_when_email_is_invalid(entityMock):
    contract = (
        Contract()
        .requires(entityMock.email_invalid, "Email", message)
        .is_email(entityMock.email_invalid, "email", message)
    )
    assert len(contract.get_notifications()) == 1
