from __future__ import annotations

import pytest
from faker import Faker

from flunt.validations.credit_card_validation_contract import (
    CreditCardValidationContract,
)

fake = Faker()


@pytest.mark.parametrize(
    ("input", "expect"),
    [
        (fake.credit_card_number(card_type="amex"), 0),
        (fake.credit_card_number(card_type="visa"), 0),
        (fake.credit_card_number(card_type="mastercard"), 0),
    ],
)
def test_should_not_receive_a_notification_when_the_credit_card_number_is_valid(
    input: str, expect: int
) -> None:
    contract = CreditCardValidationContract().is_credit_card(
        input, "CreditCard", "Value should return a valid Credit Card Number"
    )
    assert len(contract.get_notifications()) == expect


@pytest.mark.parametrize(
    ("input", "expect"),
    [
        ("5432.5678.3234.2343", 1),
        ("1234.5678.1234.5678", 1),
        ("1234 5678 1234 5678", 1),
        ("1234567812345678", 1),
    ],
)
def test_should_receive_a_notification_when_the_credit_card_number_is_invalid(
    input: str, expect: int
) -> None:
    contract = CreditCardValidationContract().is_credit_card(
        input, "CreditCard", "Value should return a valid Credit Card Number"
    )
    assert len(contract.get_notifications()) == expect
