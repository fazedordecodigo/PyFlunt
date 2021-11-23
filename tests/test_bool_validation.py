from tests.entity.sample_entity import SampleEntity
from flunt.contract import Contract
import pytest


@pytest.fixture
def _entity():
    return SampleEntity()


def test_quando_bool_e_true_deve_ser_valido(_entity):
    contract = (
        Contract()
        .requires(_entity.bool_true_property, 'Bool')
        .is_true(_entity.bool_true_property, 'Bool', 'Custom message here')
    )
    assert contract.is_valid()


def test_quando_bool_e_false_deve_ser_valido(_entity):
    contract = (
        Contract()
        .requires(_entity.bool_true_property, 'Bool')
        .is_false(_entity.bool_false_property, 'Bool', 'Custom message here')
    )
    assert contract.is_valid()


def test_quando_bool_e_true_e_invalido_deve_conter_1_notificacao(_entity):
    contract = (
        Contract()
        .requires(_entity.bool_true_property, 'Bool')
        .is_true(_entity.bool_false_property, 'Bool', 'Custom message here')
    )
    assert len(contract.get_notifications()) == 1


def test_quando_bool_e_false_e_invalido_deve_conter_1_notificacao(_entity):
    contract = (
        Contract()
        .requires(_entity.bool_true_property, 'Bool')
        .is_false(_entity.bool_true_property, 'Bool', 'Custom message here')
    )
    assert len(contract.get_notifications()) == 1


def test_quando_bool_e_none_deve_ser_valido(_entity):
    contract = (
        Contract()
        .requires(_entity.bool_true_property, 'Bool')
        .is_none(_entity.bool_none_property, 'Bool', 'Custom message here')
    )
    assert contract.is_valid()


def test_quando_bool_e_none_e_invalido_deve_conter_1_notificacao(_entity):
    contract = (
        Contract()
        .requires(_entity.bool_true_property, 'Bool')
        .is_none(_entity.bool_true_property, 'Bool', 'Custom message here')
    )
    assert len(contract.get_notifications()) == 1


def test_quando_bool_nao_e_none_deve_ser_valido(_entity):
    contract = (
        Contract()
        .requires(_entity.bool_true_property, 'Bool')
        .is_not_none(_entity.bool_true_property, 'Bool', 'Custom message here')
    )
    assert contract.is_valid()


def test_quando_bool_nao_e_none_e_invalido_deve_conter_1_notificacao(_entity):
    contract = (
        Contract()
        .requires(_entity.bool_true_property, 'Bool')
        .is_not_none(_entity.bool_none_property, 'Bool', 'Custom message here')
    )
    assert len(contract.get_notifications()) == 1
