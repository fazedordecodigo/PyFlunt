from flunt.validations.contract import Contract
from tests.mocks.entity.sample_entity import SampleEntity


def test_should_be_valid_when_is_lower_than_20(entityMock: SampleEntity):
    contract = Contract().is_lower_than(
        entityMock.first_name, 20, "first_name", "any message"
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_lower_than_5(
    entityMock: SampleEntity,
):
    contract = Contract().is_lower_than(
        entityMock.first_name, 5, "first_name", "any message"
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_lower_or_equals_than_20(
    entityMock: SampleEntity,
):
    contract = Contract().is_lower_or_equals_than(
        entityMock.first_name, 20, "first_name", "any message"
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_lower_or_equals_than_14(
    entityMock: SampleEntity,
):
    contract = Contract().is_lower_or_equals_than(
        entityMock.first_name, 14, "first_name", "any message"
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_greater_than_10(entityMock: SampleEntity):
    contract = Contract().is_greater_than(
        entityMock.first_name, 10, "first_name", "any message"
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_greater_than_15(
    entityMock: SampleEntity,
):
    contract = Contract().is_greater_than(
        entityMock.first_name, 15, "first_name", "any message"
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_greater_or_equals_than_13(
    entityMock: SampleEntity,
):
    contract = Contract().is_greater_or_equals_than(
        entityMock.first_name, 13, "first_name", "any message"
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_greater_or_equals_than_14(
    entityMock: SampleEntity,
):
    contract = Contract().is_greater_or_equals_than(
        entityMock.first_name, 14, "first_name", "any message"
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_none():
    contract = Contract().is_none(None, "first_name", "any message")  # type: ignore
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_is_none(
    entityMock: SampleEntity,
):
    contract = Contract().is_none(entityMock.first_name, "first_name", "any message")
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_not_none(entityMock: SampleEntity):
    contract = Contract().is_not_none(
        entityMock.first_name, "first_name", "any message"
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_none():
    contract = Contract().is_not_none(None, "first_name", "any message")  # type: ignore
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_valid_when_is_not_none_or_white_space(
    entityMock: SampleEntity,
):
    contract = Contract().is_not_none_or_white_space(
        entityMock.first_name, "first_name", "any message"
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_is_none():
    contract = Contract().is_not_none_or_white_space(None, "first_name", "any message")  # type: ignore
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


def test_should_be_invalid_and_return_once_notification_when_white_space():
    contract = Contract().is_not_none_or_white_space(" ", "first_name", "any message")
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


# TODO: Create tests Equal, Not Equal, Contain, Not Contain and Between
