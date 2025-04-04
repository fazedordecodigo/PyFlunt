from __future__ import annotations

from random import Random
from typing import TYPE_CHECKING

import pytest
from faker import Faker

from flunt.constants.messages import (
    GREATER_OR_EQUALS_THAN,
    GREATER_THAN,
    IS_BETWEEN,
    IS_NOT_SIZED,
    LOWER_OR_EQUALS_THAN,
    LOWER_THAN,
)
from flunt.validations.collections_validation_contract import (
    CollectionsValidationContract,
)

if TYPE_CHECKING:
    from collections.abc import Sized

    from tests.mocks.entity.sample_entity import SampleEntity

fake = Faker()

random_generator = Random(42)


@pytest.fixture
def key() -> str:
    return "first_name"


@pytest.fixture
def message() -> str:
    return "any message"


range_one_to_nineteen = random_generator.randint(1, 19)
range_twenty_to_fifty = random_generator.randint(20, 50)
range_fifty_one_to_hundred = random_generator.randint(51, 100)


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


def test_should_return_a_custom_message_when_value_is_not_between(
    entity_mock: SampleEntity,
) -> None:
    message = "any message"
    contract = CollectionsValidationContract().is_between(
        entity_mock.collection_property, 1, 2, "key", message
    )
    assert contract.get_notifications()[0].message == message


def test_should_return_a_standard_message_when_value_is_not_between(
    entity_mock: SampleEntity,
) -> None:
    contract = CollectionsValidationContract().is_between(
        entity_mock.full_name, 1, 10, "key"
    )
    assert contract.get_notifications()[0].message == IS_BETWEEN.format(
        "key", 1, 10
    )


def test_should_return_a_message_when_value_is_not_sized_in_is_between() -> (
    None
):
    contract = CollectionsValidationContract().is_between(True, 1, 2, "key")  # type: ignore[arg-type]
    assert contract.get_notifications()[0].message == IS_NOT_SIZED


def test_should_not_return_a_message_when_value_is_none_in_is_between() -> (
    None
):
    contract = CollectionsValidationContract().is_between(None, 1, 2, "key")  # type: ignore[arg-type]
    assert len(contract.get_notifications()) == 0


def test_should_return_a_message_when_value_is_not_sized_in_is_greater_or_equals_than(
    entity_mock: SampleEntity,
) -> None:
    contract = CollectionsValidationContract().is_greater_or_equals_than(
        True,  # type: ignore[arg-type]
        1,
        entity_mock.full_name,
        "key",
    )
    assert contract.get_notifications()[0].message == IS_NOT_SIZED


def test_should_not_return_a_message_when_value_is_none_in_is_greater_or_equals_than(
    entity_mock: SampleEntity,
) -> None:
    contract = CollectionsValidationContract().is_greater_or_equals_than(
        None,  # type: ignore[arg-type]
        1,
        entity_mock.full_name,
        "key",
    )
    assert len(contract.get_notifications()) == 0


def test_should_return_a_message_when_value_is_not_sized_in_is_greater_than(
    entity_mock: SampleEntity,
) -> None:
    contract = CollectionsValidationContract().is_greater_than(
        True,  # type: ignore[arg-type]
        1,
        entity_mock.full_name,
        "key",
    )
    assert contract.get_notifications()[0].message == IS_NOT_SIZED


def test_should_not_return_a_message_when_value_is_none_in_is_greater_than(
    entity_mock: SampleEntity,
) -> None:
    contract = CollectionsValidationContract().is_greater_than(
        None,  # type: ignore[arg-type]
        1,
        entity_mock.full_name,
        "key",
    )
    assert len(contract.get_notifications()) == 0


def test_should_return_a_message_when_value_is_not_sized_in_is_lower_than(
    entity_mock: SampleEntity,
) -> None:
    contract = CollectionsValidationContract().is_lower_than(
        True,  # type: ignore[arg-type]
        1,
        entity_mock.full_name,
        "key",
    )
    assert contract.get_notifications()[0].message == IS_NOT_SIZED


def test_should_not_return_a_message_when_value_is_none_in_is_lower_than(
    entity_mock: SampleEntity,
) -> None:
    contract = CollectionsValidationContract().is_lower_than(
        None,  # type: ignore[arg-type]
        1,
        entity_mock.full_name,
        "key",
    )
    assert len(contract.get_notifications()) == 0


def test_should_return_a_message_when_value_is_not_sized_in_is_lower_or_equals_than(
    entity_mock: SampleEntity,
) -> None:
    contract = CollectionsValidationContract().is_lower_or_equals_than(
        True,  # type: ignore[arg-type]
        1,
        entity_mock.full_name,
        "key",
    )
    assert contract.get_notifications()[0].message == IS_NOT_SIZED


def test_should_not_return_a_message_when_value_is_none_in_is_lower_or_equals_than(
    entity_mock: SampleEntity,
) -> None:
    contract = CollectionsValidationContract().is_lower_or_equals_than(
        None,  # type: ignore[arg-type]
        1,
        entity_mock.full_name,
        "key",
    )
    assert len(contract.get_notifications()) == 0


def test_should_return_a_standard_message_when_not_is_lower_than() -> None:
    value = "abcdef"  # tamanho 6
    comparer = 5
    field = "key"
    contract = CollectionsValidationContract().is_lower_than(
        value, comparer, field
    )
    assert contract.get_notifications()[0].message == LOWER_THAN.format(
        field, comparer
    )


def test_should_return_a_standard_message_when_not_is_lower_or_equals_than() -> (
    None
):
    value = "abcdef"  # tamanho 6
    comparer = 5
    field = "key"
    contract = CollectionsValidationContract().is_lower_or_equals_than(
        value, comparer, field
    )
    assert contract.get_notifications()[
        0
    ].message == LOWER_OR_EQUALS_THAN.format(field, comparer)


def test_should_return_a_standard_message_when_not_is_greater_than() -> None:
    value = "abc"  # tamanho 3
    comparer = 5
    field = "key"
    contract = CollectionsValidationContract().is_greater_than(
        value, comparer, field
    )
    assert contract.get_notifications()[0].message == GREATER_THAN.format(
        field, comparer
    )


def test_should_return_a_standard_message_when_not_is_greater_or_equals_than() -> (
    None
):
    value = "abc"  # tamanho 3
    comparer = 5
    field = "key"
    contract = CollectionsValidationContract().is_greater_or_equals_than(
        value, comparer, field
    )
    assert contract.get_notifications()[
        0
    ].message == GREATER_OR_EQUALS_THAN.format(field, comparer)


def test_should_use_custom_message_in_is_lower_than() -> None:
    message = "Mensagem personalizada"
    contract = CollectionsValidationContract().is_lower_than(
        "abcdef",  # tamanho 6
        5,
        "campo",
        message,
    )
    assert contract.get_notifications()[0].message == message


def test_should_use_custom_message_in_is_lower_or_equals_than() -> None:
    message = "Mensagem personalizada"
    contract = CollectionsValidationContract().is_lower_or_equals_than(
        "abcdef",  # tamanho 6
        5,
        "campo",
        message,
    )
    assert contract.get_notifications()[0].message == message


def test_should_use_custom_message_in_is_greater_than() -> None:
    message = "Mensagem personalizada"
    contract = CollectionsValidationContract().is_greater_than(
        "abc",  # tamanho 3
        5,
        "campo",
        message,
    )
    assert contract.get_notifications()[0].message == message


def test_should_use_custom_message_in_is_greater_or_equals_than() -> None:
    message = "Mensagem personalizada"
    contract = CollectionsValidationContract().is_greater_or_equals_than(
        "abc",  # tamanho 3
        5,
        "campo",
        message,
    )
    assert contract.get_notifications()[0].message == message


def test_should_use_same_format_message_in_is_between() -> None:
    field = "campo"
    min_value = 10
    max_value = 20

    test_value = "abc"  # tamanho 3
    contract = CollectionsValidationContract().is_between(
        test_value, min_value, max_value, field, IS_BETWEEN
    )

    assert contract.get_notifications()[0].message == IS_BETWEEN.format(
        field, min_value, max_value
    )
