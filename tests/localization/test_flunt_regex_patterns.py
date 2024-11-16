from __future__ import annotations

import re

import pytest
from faker import Faker

fake = Faker("pt_BR")


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (fake.email(), True),
        (fake.url(), False),
        (fake.name(), False),
    ],
)
def test_should_identify_a_valid_email_address(regex, value, expect):
    result = re.match(regex.email_regex_pattern, value)
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
def test_should_identify_a_valid_cpf(regex, value, expect):
    result = re.match(regex.cpf_regex_pattern, value)
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
def test_should_identify_a_valid_cnpj(regex, value, expect):
    result = re.match(regex.cnpj_regex_pattern, value)
    assert isinstance(result, re.Match) is expect


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        (fake.url(), True),
        (fake.email(), False),
        (fake.name(), False),
    ],
)
def test_should_identify_a_valid_url(regex, value, expect):
    result = re.match(regex.url_regex_pattern, value)
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
def test_should_identify_only_numbers(regex, value, expect):
    result = re.match(regex.only_number_regex_pattern, value)
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
def test_should_identify_letters_and_numbers(regex, value, expect):
    result = re.match(regex.only_letters_and_numbers_regex_pattern, value)
    assert isinstance(result, re.Match) is expect


@pytest.mark.parametrize(
    ("value", "expect"),
    [
        ("JM112035", True),
        (fake.name(), False),
    ],
)
def test_should_identify_a_valid_passport(regex, value, expect):
    result = re.match(regex.passport_regex_pattern, value)
    assert isinstance(result, re.Match) is expect
