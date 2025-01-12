from __future__ import annotations

from collections.abc import Sized
from random import randint

import pytest
from faker import Faker

from flunt.validations.collections_validation_contract import (
    CollectionsValidationContract,
)

fake = Faker()


@pytest.fixture
def key() -> str:
    return "first_name"


@pytest.fixture
def message() -> str:
    return "any message"


range_one_to_nineteen = randint(1, 19)
range_twenty_to_fifty = randint(20, 50)
range_fifty_one_to_hundred = randint(51, 100)


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (
            fake.pydict(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pyiterable(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pylist(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pyset(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (fake.pystr(max_chars=range_one_to_nineteen), range_twenty_to_fifty),
        (
            fake.pytuple(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
    ],
)
def test_should_be_valid_when_is_lower_than(
    value: str | list | dict | set | tuple | range | bytearray,
    expect: int,
    key: str,
    message: str,
) -> None:
    contract = CollectionsValidationContract().is_lower_than(
        value, expect, key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (
            fake.pydict(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pyiterable(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pylist(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pyset(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (fake.pystr(max_chars=range_twenty_to_fifty), range_one_to_nineteen),
        (
            fake.pytuple(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (fake.pydict(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pyiterable(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pylist(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pyset(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pystr(max_chars=10), 10),
        (fake.pytuple(nb_elements=10, variable_nb_elements=False), 10),
    ],
)
def test_should_be_invalid_and_return_once_notification_when_not_is_lower_than(
    value: str | list | dict | set | tuple | range | bytearray,
    expect: int,
    key: str,
    message: str,
) -> None:
    contract = CollectionsValidationContract().is_lower_than(
        value, expect, key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (
            fake.pydict(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pyiterable(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pylist(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pyset(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (fake.pystr(max_chars=range_one_to_nineteen), range_twenty_to_fifty),
        (
            fake.pytuple(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (fake.pydict(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pyiterable(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pylist(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pyset(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pystr(max_chars=10), 10),
        (fake.pytuple(nb_elements=10, variable_nb_elements=False), 10),
    ],
)
def test_should_be_valid_when_is_lower_or_equals_than(
    value: str | list | dict | set | tuple | range | bytearray,
    expect: int,
    key: str,
    message: str,
) -> None:
    contract = CollectionsValidationContract().is_lower_or_equals_than(
        value, expect, key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (
            fake.pydict(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pyiterable(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pylist(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pyset(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (fake.pystr(max_chars=range_twenty_to_fifty), range_one_to_nineteen),
        (
            fake.pytuple(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
    ],
)
def test_should_be_invalid_and_return_once_notification_when_not_is_lower_or_equals_than(
    value: str | list | dict | set | tuple | range | bytearray,
    expect: int,
    key: str,
    message: str,
) -> None:
    contract = CollectionsValidationContract().is_lower_or_equals_than(
        value, expect, key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (
            fake.pydict(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pyiterable(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pylist(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pyset(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (fake.pystr(max_chars=range_twenty_to_fifty), range_one_to_nineteen),
        (
            fake.pytuple(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
    ],
)
def test_should_be_valid_when_is_greater_than(
    value: str | list | dict | set | tuple | range | bytearray,
    expect: int,
    key: str,
    message: str,
) -> None:
    contract = CollectionsValidationContract().is_greater_than(
        value, expect, key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (
            fake.pydict(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pyiterable(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pylist(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pyset(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (fake.pystr(max_chars=range_one_to_nineteen), range_twenty_to_fifty),
        (
            fake.pytuple(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (fake.pydict(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pyiterable(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pylist(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pyset(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pystr(max_chars=10), 10),
        (fake.pytuple(nb_elements=10, variable_nb_elements=False), 10),
    ],
)
def test_should_be_invalid_and_return_once_notification_when_not_is_greater_than(
    value: str | list | dict | set | tuple | range | bytearray,
    expect: int,
    key: str,
    message: str,
) -> None:
    contract = CollectionsValidationContract().is_greater_than(
        value, expect, key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (
            fake.pydict(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pyiterable(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pylist(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (
            fake.pyset(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (fake.pystr(max_chars=range_twenty_to_fifty), range_one_to_nineteen),
        (
            fake.pytuple(
                nb_elements=range_twenty_to_fifty, variable_nb_elements=False
            ),
            range_one_to_nineteen,
        ),
        (fake.pydict(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pyiterable(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pylist(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pyset(nb_elements=10, variable_nb_elements=False), 10),
        (fake.pystr(max_chars=10), 10),
        (fake.pytuple(nb_elements=10, variable_nb_elements=False), 10),
    ],
)
def test_should_be_valid_when_is_greater_or_equals_than(
    value: str | list | dict | set | tuple | range | bytearray,
    expect: int,
    key: str,
    message: str,
) -> None:
    contract = CollectionsValidationContract().is_greater_or_equals_than(
        value, expect, key, message
    )
    assert contract.is_valid
    assert len(contract.get_notifications()) == 0


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (
            fake.pydict(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pyiterable(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pylist(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (
            fake.pyset(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
        (fake.pystr(max_chars=range_one_to_nineteen), range_twenty_to_fifty),
        (
            fake.pytuple(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
        ),
    ],
)
def test_should_be_invalid_and_return_once_notification_when_not_is_greater_or_equals_than(
    value: str | list | dict | set | tuple | range | bytearray,
    expect: int,
    key: str,
    message: str,
) -> None:
    contract = CollectionsValidationContract().is_greater_or_equals_than(
        value, expect, key, message
    )
    assert contract.is_valid is False
    assert len(contract.get_notifications()) == 1


@pytest.mark.parametrize(
    ("value", "value_min", "value_max"),
    [
        (
            fake.pydict(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_one_to_nineteen,
            range_twenty_to_fifty,
        ),
        (
            fake.pyiterable(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_one_to_nineteen,
            range_twenty_to_fifty,
        ),
        (
            fake.pylist(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_one_to_nineteen,
            range_twenty_to_fifty,
        ),
        (
            fake.pyset(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_one_to_nineteen,
            range_twenty_to_fifty,
        ),
        (
            fake.pystr(max_chars=range_one_to_nineteen),
            range_one_to_nineteen,
            range_twenty_to_fifty,
        ),
        (
            fake.pytuple(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_one_to_nineteen,
            range_twenty_to_fifty,
        ),
    ],
)
def test_should_be_valid_and_not_return_notification_when_value_is_between(
    value: str | list | dict | set | tuple | range | bytearray,
    value_min: int,
    value_max: int,
    key: str,
    message: str,
) -> None:
    contract = CollectionsValidationContract().is_between(
        value, value_min, value_max, key, message
    )
    assert contract.is_valid


@pytest.mark.parametrize(
    ("value", "value_min", "value_max"),
    [
        (
            fake.pydict(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
            range_fifty_one_to_hundred,
        ),
        (
            fake.pyiterable(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
            range_fifty_one_to_hundred,
        ),
        (
            fake.pylist(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
            range_fifty_one_to_hundred,
        ),
        (
            fake.pyset(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
            range_fifty_one_to_hundred,
        ),
        (
            fake.pystr(max_chars=range_one_to_nineteen),
            range_twenty_to_fifty,
            range_fifty_one_to_hundred,
        ),
        (
            fake.pytuple(
                nb_elements=range_one_to_nineteen, variable_nb_elements=False
            ),
            range_twenty_to_fifty,
            range_fifty_one_to_hundred,
        ),
    ],
)
def test_should_be_invalid_and_return_once_notification_when_value_is_not_between(
    value: Sized,
    value_min: int,
    value_max: int,
) -> None:
    contract = CollectionsValidationContract().is_between(
        value, value_min, value_max, "key"
    )
    assert len(contract.get_notifications()) == 1
