from __future__ import annotations

from tests.mocks.value_objects.vo import Name


def test_quando_nome_possuir_mais_que_2_e_menos_que_51_caracteres_deve_ser_valido() -> (
    None
):
    nome = Name("Emerson", "Delatorre")
    assert nome.is_valid


def test_quando_first_name_nao_for_preenchido_deve_ser_invalido() -> None:
    nome = Name(None, "Delatorre")  # type: ignore
    assert nome.is_valid is False


def test_quando_last_name_nao_for_preenchido_deve_ser_invalido() -> None:
    nome = Name("Emerson", None)  # type: ignore
    assert nome.is_valid is False


def test_quando_first_name_possuir_menos_que_3_caracteres_deve_ser_invalido() -> (
    None
):
    nome = Name("Sr", "Delatorre")
    assert nome.is_valid is False


def test_quando_first_name_possuir_mais_que_50_caracteres_deve_ser_invalido() -> (
    None
):
    nome = Name(
        "Emerson Delatorre de Andrade Moraes Santana Gonçalves", "Delatorre"
    )
    assert nome.is_valid is False


def test_quando_last_name_possuir_menos_que_3_caracteres_deve_ser_invalido() -> (
    None
):
    nome = Name("Emerson", "Jr")
    assert nome.is_valid is False


def test_quando_last_name_possuir_mais_que_50_caracteres_deve_ser_invalido() -> (
    None
):
    nome = Name(
        "Emerson", "Emerson Delatorre de Andrade Moraes Santana Gonçalves"
    )
    assert nome.is_valid is False
