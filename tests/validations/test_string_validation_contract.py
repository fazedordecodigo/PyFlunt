
from flunt.validations.contract import Contract


def test_should_be_valid_when_is_lower_then_20(entityMock):
    contract = (
        Contract()
        .is_lower_than(entityMock.first_name, 20, "first_name", "any message")
    )
    assert contract.is_valid()
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_lower_then_5(entityMock):
    contract = (
        Contract()
        .is_lower_than(entityMock.first_name, 5, "first_name", "any message")
    )
    assert contract.is_valid() is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_lower_or_equals_then_20(entityMock):
    contract = (
        Contract()
        .is_lower_or_equals_than(entityMock.first_name, 20, "first_name", "any message")
    )
    assert contract.is_valid()
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_lower_or_equals_then_14(entityMock):
    contract = (
        Contract()
        .is_lower_or_equals_than(entityMock.first_name, 14, "first_name", "any message")
    )
    assert contract.is_valid() is False
    assert len(contract.get_notifications()) == 1