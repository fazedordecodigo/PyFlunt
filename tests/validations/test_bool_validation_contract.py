from flunt.validations.contract import Contract


def test_should_be_valid_when_is_true(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_true(entityMock.bool_true_property, "Bool", "Custom message here")
    )
    assert contract.is_valid()


def test_should_be_valid_when_is_false(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_false(entityMock.bool_false_property, "Bool", "Custom message here")
    )
    assert contract.is_valid()


def test_should_return_a_once_notification_when_is_true_is_invalid(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_true(entityMock.bool_false_property, "Bool", "Custom message here")
    )
    assert len(contract.get_notifications()) == 1


def test_should_return_a_once_notification_when_is_false_is_invalid(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_false(entityMock.bool_true_property, "Bool", "Custom message here")
    )
    assert len(contract.get_notifications()) == 1


def test_should_return_valid_when_is_none_is_valid(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_none(entityMock.bool_none_property, "Bool", "Custom message here")
    )
    assert contract.is_valid()


def test_should_return_a_once_notification_when_is_none_is_invalid(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_none(entityMock.bool_true_property, "Bool", "Custom message here")
    )
    assert len(contract.get_notifications()) == 1


def test_should_return_valid_when_is_not_none_is_valid(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_not_none(entityMock.bool_true_property, "Bool", "Custom message here")
    )
    assert contract.is_valid()


def test_should_return_a_once_notification_when_is_not_none_is_invalid(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_not_none(entityMock.bool_none_property, "Bool", "Custom message here")
    )
    assert len(contract.get_notifications()) == 1
