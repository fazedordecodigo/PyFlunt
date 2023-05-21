from flunt.validations.contract import Contract


def test_quando_bool_e_true_deve_ser_valido(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_true(entityMock.bool_true_property, "Bool", "Custom message here")
    )
    assert contract.is_valid()


def test_quando_bool_e_false_deve_ser_valido(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_false(entityMock.bool_false_property, "Bool", "Custom message here")
    )
    assert contract.is_valid()


def test_quando_bool_e_true_e_invalido_deve_conter_1_notificacao(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_true(entityMock.bool_false_property, "Bool", "Custom message here")
    )
    assert len(contract.get_notifications()) == 1


def test_quando_bool_e_false_e_invalido_deve_conter_1_notificacao(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_false(entityMock.bool_true_property, "Bool", "Custom message here")
    )
    assert len(contract.get_notifications()) == 1


def test_quando_bool_e_none_deve_ser_valido(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_none(entityMock.bool_none_property, "Bool", "Custom message here")
    )
    assert contract.is_valid()


def test_quando_bool_e_none_e_invalido_deve_conter_1_notificacao(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_none(entityMock.bool_true_property, "Bool", "Custom message here")
    )
    assert len(contract.get_notifications()) == 1


def test_quando_bool_nao_e_none_deve_ser_valido(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_not_none(entityMock.bool_true_property, "Bool", "Custom message here")
    )
    assert contract.is_valid()


def test_quando_bool_nao_e_none_e_invalido_deve_conter_1_notificacao(entityMock):
    contract = (
        Contract()
        .requires(entityMock.bool_true_property, "Bool")
        .is_not_none(entityMock.bool_none_property, "Bool", "Custom message here")
    )
    assert len(contract.get_notifications()) == 1
