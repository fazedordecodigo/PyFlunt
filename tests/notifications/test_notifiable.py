"""Module Test Notifiable."""
from tests.models.vo import Name


def test_vo_deve_ser_valido():
    """Test Is Valid."""
    nome = Name('Emerson', 'Delatorre')

    assert nome.is_valid()
