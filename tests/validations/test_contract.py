
import pytest
from uuid import uuid4
from faker import Faker

from flunt.validations.contract import Contract


fake = Faker()

@pytest.mark.parametrize(
	'input',
	[
		fake.uuid4(),
		fake.date_object(),
        fake.json(),
        fake.pydecimal(),
        fake.pydict(),
        fake.pyfloat(),
        fake.pyint(),
        fake.pyiterable(),
        fake.pylist(),
        fake.pyset(),
        fake.pystr(),
        fake.pystr_format(),
        fake.pystruct(),
        fake.pytuple(),
        True,
        False,
        uuid4()
	],
)
def test_should_be_valid_and_not_return_notification_when_required_is_not_none(input):
    contract = Contract().requires(input, fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))
    assert contract.is_valid


@pytest.mark.parametrize(
	'input',
	[
		None,
        '',
	],
)
def test_should_be_invalid_and_return_once_notification_when_required_is_none_or_empty(input):
    contract = Contract().requires(input, fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))
    assert contract.is_valid is False
