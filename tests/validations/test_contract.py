from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID, uuid4

import pytest
from faker import Faker

from flunt.validations.contract import Contract

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable
    from decimal import Decimal
    from struct import Struct

fake = Faker()


@pytest.mark.parametrize(
    "input",
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
        uuid4(),
    ],
)
def test_should_be_valid_and_not_return_notification_when_required_is_not_none(
    input: Any,
) -> None:
    contract = Contract().requires(
        input,
        fake.text(max_nb_chars=10),
        fake.text(max_nb_chars=20),
    )
    assert contract.is_valid


@pytest.mark.parametrize(
    "input",
    [
        None,
        "",
    ],
)
def test_should_be_invalid_and_return_once_notification_when_required_is_none_or_empty(
    input: bool
    | str
    | float
    | tuple
    | set
    | list
    | Iterable
    | dict
    | Callable
    | Decimal
    | UUID
    | object
    | Struct,
) -> None:
    contract = Contract().requires(
        input, fake.text(max_nb_chars=10), fake.text(max_nb_chars=20)
    )
    assert contract.is_valid is False
