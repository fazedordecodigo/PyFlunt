import pytest
from faker import Faker
from uuid import uuid4
from flunt.validations.commons_validation_contract import CommonsValidationContract


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
        fake.pybool(),
        uuid4()
	],
)
def test_should_return_true_when_are_equals_receives_two_values_are_equal_regardless_of_the_type(input):
    contract =  CommonsValidationContract()
    contract.are_equals(input, input, fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))

    assert contract.is_valid

@pytest.mark.parametrize(
	'input,expected',
	[
		(fake.uuid4(), fake.uuid4()),
		(fake.date_object(), fake.date_object()),
        (fake.json(), fake.json()),
        (fake.pydecimal(), fake.pydecimal()),
        (fake.pydict(), fake.pydict()),
        (fake.pyfloat(), fake.pyfloat()),
        (fake.pyint(), fake.pyint()),
        (fake.pyiterable(), fake.pyiterable()),
        (fake.pylist(), fake.pylist()),
        (fake.pyset(), fake.pyset()),
        (fake.pystr(), fake.pystr()),
        (fake.pystr_format(), fake.pystr_format()),
        (fake.pystruct(), fake.pystruct()),
        (fake.pytuple(), fake.pytuple()),
        (fake.pybool(100), fake.pybool(0)),
        (fake.uuid4(), fake.date_object()),
        (fake.json(), fake.pydecimal()),
        (fake.pydict(), uuid4()),
	],
)
def test_should_return_false_when_are_equals_receives_two_values_are_not_equal_regardless_of_the_type(input, expected):
    contract =  CommonsValidationContract()
    contract.are_equals(input, expected, fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))

    assert contract.is_valid is False

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
        fake.pybool(),
        uuid4()
	],
)
def test_should_return_true_when_are_not_equals_receives_two_values_are_equal_regardless_of_the_type(input):
    contract =  CommonsValidationContract()
    contract.are_not_equals(input, input, fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))

    assert contract.is_valid is False

@pytest.mark.parametrize(
	'input,expected',
	[
		(fake.uuid4(), fake.uuid4()),
		(fake.date_object(), fake.date_object()),
        (fake.json(), fake.json()),
        (fake.pydecimal(), fake.pydecimal()),
        (fake.pydict(), fake.pydict()),
        (fake.pyfloat(), fake.pyfloat()),
        (fake.pyint(), fake.pyint()),
        (fake.pyiterable(), fake.pyiterable()),
        (fake.pylist(), fake.pylist()),
        (fake.pyset(), fake.pyset()),
        (fake.pystr(), fake.pystr()),
        (fake.pystr_format(), fake.pystr_format()),
        (fake.pystruct(), fake.pystruct()),
        (fake.pytuple(), fake.pytuple()),
        (fake.pybool(100), fake.pybool(0)),
        (fake.uuid4(), fake.date_object()),
        (fake.json(), fake.pydecimal()),
        (fake.pydict(), uuid4()),
	],
)
def test_should_return_true_when_are_not_equals_receives_two_values_are_not_equal_regardless_of_the_type(input, expected):
    contract =  CommonsValidationContract()
    contract.are_not_equals(input, expected, fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))

    assert contract.is_valid

def test_should_return_true_when_is_none_receives_value_none():
    contract =  CommonsValidationContract()
    contract.is_none(None, fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))

    assert contract.is_valid

def test_should_return_false_when_is_none_receives_value_is_not_none():
    contract =  CommonsValidationContract()
    contract.is_none(fake.text(max_nb_chars=10), fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))

    assert contract.is_valid is False

def test_should_return_true_when_is_not_none_receives_value_is_not_none():
    contract =  CommonsValidationContract()
    contract.is_not_none(fake.text(max_nb_chars=10), fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))

    assert contract.is_valid

def test_should_return_false_when_is_not_none_receives_value_is_none():
    contract =  CommonsValidationContract()
    contract.is_not_none(None, fake.text(max_nb_chars=10), fake.text(max_nb_chars=20))

    assert contract.is_valid is False
