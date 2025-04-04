from __future__ import annotations

import re

import pytest
from faker import Faker

from flunt.localization.flunt_regex_patterns import get_pattern

fake = Faker("pt_BR")


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (fake.email(), True),
        (fake.url(), False),
        (fake.name(), False),
    ],
)
def test_should_identify_a_valid_email_address(
    value: str, expect: bool
) -> None:
    regex = get_pattern("email")
    result = re.match(regex, value)
    assert isinstance(result, re.Match) is expect


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (fake.cpf(), True),
        (fake.ssn(), True),
        (fake.rg(), False),
        (fake.cnpj(), False),
    ],
)
def test_should_identify_a_valid_cpf(value: str, expect: bool) -> None:
    regex = get_pattern("cpf")
    result = re.match(regex, value)
    assert isinstance(result, re.Match) is expect


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (fake.cnpj(), True),
        (fake.company_id(), True),
        (fake.rg(), False),
        (fake.cpf(), False),
    ],
)
def test_should_identify_a_valid_cnpj(value: str, expect: bool) -> None:
    regex = get_pattern("cnpj")
    result = re.match(regex, value)
    assert isinstance(result, re.Match) is expect


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (fake.url(), True),
        (fake.email(), False),
        (fake.name(), False),
    ],
)
def test_should_identify_a_valid_url(value: str, expect: bool) -> None:
    regex = get_pattern("url")
    result = re.match(regex, value)
    assert isinstance(result, re.Match) is expect


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (fake.ssn(), True),
        (fake.company_id(), True),
        (fake.user_name(), False),
        (fake.ipv4_public(), False),
    ],
)
def test_should_identify_only_numbers(value: str, expect: bool) -> None:
    regex = get_pattern("only_numbers")
    result = re.match(regex, value)
    assert isinstance(result, re.Match) is expect


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (fake.mac_address(), True),
        (fake.name(), True),
        (fake.ipv4_public(), True),
        ("", False),
    ],
)
def test_should_identify_letters_and_numbers(value: str, expect: bool) -> None:
    regex = get_pattern("only_letters_and_numbers")
    result = re.match(regex, value)
    assert isinstance(result, re.Match) is expect


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        ("JM112035", True),
        (fake.name(), False),
    ],
)
def test_should_identify_a_valid_passport(value: str, expect: bool) -> None:
    regex = get_pattern("passport")
    result = re.match(regex, value)
    assert isinstance(result, re.Match) is expect
