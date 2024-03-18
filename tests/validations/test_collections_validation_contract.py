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
range_fiftyone_to_onehundred = randint(51, 100)

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


@pytest.mark.parametrize(
	'input, min, max',
	[
		(fake.pydict(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_one_to_nineteen, range_twenty_to_fifty),
		(fake.pyiterable(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_one_to_nineteen, range_twenty_to_fifty),
		(fake.pylist(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_one_to_nineteen, range_twenty_to_fifty),
		(fake.pyset(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_one_to_nineteen, range_twenty_to_fifty),
		(fake.pystr(max_chars=range_one_to_nineteen), range_one_to_nineteen, range_twenty_to_fifty),
		(fake.pytuple(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_one_to_nineteen, range_twenty_to_fifty)
	],
)
def test_should_be_valid_and_not_return_notification_when_value_is_between(input, min, max):
	contract = CollectionsValidationContract().is_between(input, min, max, "test", "any_message")
	assert contract.is_valid


@pytest.mark.parametrize(
	'input, min, max',
	[
		(fake.pydict(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty, range_fiftyone_to_onehundred),
		(fake.pyiterable(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty, range_fiftyone_to_onehundred),
		(fake.pylist(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty, range_fiftyone_to_onehundred),
		(fake.pyset(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty, range_fiftyone_to_onehundred),
		(fake.pystr(max_chars=range_one_to_nineteen), range_twenty_to_fifty, range_fiftyone_to_onehundred),
		(fake.pytuple(nb_elements=range_one_to_nineteen, variable_nb_elements=False), range_twenty_to_fifty, range_fiftyone_to_onehundred)
	],
)
def test_should_be_invalid_and_return_once_notification_when_value_is_not_between(input, min, max):
	contract = CollectionsValidationContract().is_between(input, min, max, "test", "any_message")
	assert contract.is_valid is False
