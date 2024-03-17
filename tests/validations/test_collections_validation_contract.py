from faker import Faker
import pytest
from flunt.validations.collections_validation_contract import CollectionsValidationContract
from tests.mocks.entity.sample_entity import SampleEntity
from random import randint


fake = Faker()

@pytest.fixture()
def key():
    yield 'first_name'


@pytest.fixture()
def message():
	yield 'any message'


range_one_to_nineteen = randint(1, 19)
range_twenty_to_fifty = randint(20, 50)

@pytest.mark.parametrize(
	'input, expect',
	[
		(fake.pydict(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pyiterable(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pylist(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pyset(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pystr(max_chars=range_one_to_nineteen), range_twenty_to_fifty),
		(fake.pytuple(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
	],
)
def test_should_be_valid_when_is_lower_than(input, expect, key, message):
	contract = CollectionsValidationContract().is_lower_than(
		input, expect, key, message
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


@pytest.mark.parametrize(
	'input, expect',
	[
		(fake.pydict(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pyiterable(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pylist(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pyset(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pystr(max_chars=range_twenty_to_fifty), range_one_to_nineteen),
		(fake.pytuple(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pydict(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pyiterable(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pylist(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pyset(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pystr(max_chars=10), 10),
		(fake.pytuple(nb_elements=10, variable_nb_elements=False), 10)
	],
)
def test_should_be_invalid_and_return_once_notification_when_not_is_lower_than(
	input, expect, key, message
):
	contract = CollectionsValidationContract().is_lower_than(
		input, expect, key, message
	)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


@pytest.mark.parametrize(
	'input, expect',
	[
		(fake.pydict(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pyiterable(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pylist(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pyset(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pystr(max_chars=range_one_to_nineteen), range_twenty_to_fifty),
		(fake.pytuple(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pydict(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pyiterable(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pylist(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pyset(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pystr(max_chars=10), 10),
		(fake.pytuple(nb_elements=10, variable_nb_elements=False), 10)
	],
)
def test_should_be_valid_when_is_lower_or_equals_than(
	input, expect, key, message
):
	contract = CollectionsValidationContract().is_lower_or_equals_than(
		input, expect, key, message
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


@pytest.mark.parametrize(
	'input, expect',
	[
		(fake.pydict(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pyiterable(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pylist(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pyset(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pystr(max_chars=range_twenty_to_fifty), range_one_to_nineteen),
		(fake.pytuple(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
	],
)
def test_should_be_invalid_and_return_once_notification_when_not_is_lower_or_equals_than(
	input, expect, key, message
):
	contract = CollectionsValidationContract().is_lower_or_equals_than(
		input, expect, key, message
	)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


@pytest.mark.parametrize(
	'input, expect',
	[
		(fake.pydict(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pyiterable(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pylist(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pyset(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pystr(max_chars=range_twenty_to_fifty), range_one_to_nineteen),
		(fake.pytuple(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen)
	],
)
def test_should_be_valid_when_is_greater_than(input, expect, key, message):
	contract = CollectionsValidationContract().is_greater_than(
		input, expect, key, message
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


@pytest.mark.parametrize(
	'input, expect',
	[
		(fake.pydict(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pyiterable(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pylist(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pyset(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pystr(max_chars=range_one_to_nineteen), range_twenty_to_fifty),
		(fake.pytuple(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pydict(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pyiterable(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pylist(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pyset(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pystr(max_chars=10), 10),
		(fake.pytuple(nb_elements=10, variable_nb_elements=False), 10)
	],
)
def test_should_be_invalid_and_return_once_notification_when_not_is_greater_than(
	input, expect, key, message
):
	contract = CollectionsValidationContract().is_greater_than(
		input, expect, key, message
	)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


@pytest.mark.parametrize(
	'input, expect',
	[
		(fake.pydict(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pyiterable(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pylist(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pyset(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pystr(max_chars=range_twenty_to_fifty), range_one_to_nineteen),
		(fake.pytuple(nb_elements=range_twenty_to_fifty, variable_nb_elements=False), range_one_to_nineteen),
		(fake.pydict(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pyiterable(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pylist(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pyset(nb_elements=10, variable_nb_elements=False), 10),
		(fake.pystr(max_chars=10), 10),
		(fake.pytuple(nb_elements=10, variable_nb_elements=False), 10)
	],
)
def test_should_be_valid_when_is_greater_or_equals_than(
	input, expect, key, message
):
	contract = CollectionsValidationContract().is_greater_or_equals_than(
		input, expect, key, message
	)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


@pytest.mark.parametrize(
	'input, expect',
	[
		(fake.pydict(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pyiterable(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pylist(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pyset(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty),
		(fake.pystr(max_chars=range_one_to_nineteen), range_twenty_to_fifty),
		(fake.pytuple(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty)
	],
)
def test_should_be_invalid_and_return_once_notification_when_not_is_greater_or_equals_than(
	input, expect, key, message
):
	contract = CollectionsValidationContract().is_greater_or_equals_than(
		input, expect, key, message
	)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


def test_should_be_valid_and_not_return_notification_when_contains_a_search_string(entity_mock: SampleEntity, key, message):
	contract = CollectionsValidationContract().contains(entity_mock.first_name, "any", key, message)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_not_contains_a_search_string(entity_mock: SampleEntity, key, message):
	contract = CollectionsValidationContract().contains(entity_mock.first_name, "bla", key, message)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


def test_should_be_valid_and_not_return_notification_when_not_contains_a_search_string(entity_mock: SampleEntity, key, message):
	contract = CollectionsValidationContract().not_contains(entity_mock.first_name, "bla", key, message)
	assert contract.is_valid
	assert len(contract.get_notifications()) == 0


def test_should_be_invalid_and_return_once_notification_when_contains_a_search_string(entity_mock: SampleEntity, key, message):
	contract = CollectionsValidationContract().not_contains(entity_mock.first_name, "any", key, message)
	assert contract.is_valid is False
	assert len(contract.get_notifications()) == 1


def test_should_be_valid_and_not_return_notification_when_value_is_between():
	contract = CollectionsValidationContract().is_between("any_text", 1, 10, "test", "any_message")
	assert contract.is_valid


def test_should_be_invalid_and_return_once_notification_when_value_is_not_between():
	contract = CollectionsValidationContract().is_between("any_text", 10, 20, "test", "any_message")
	assert contract.is_valid is False
