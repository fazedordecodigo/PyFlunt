import re


def test_should_identify_a_valid_email_address_returning_not_none(regex):
    actual: str = "any@any.com"
    expected = re.match(regex.email_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_email_address_returning_none(regex):
    actual: str = "any.com"
    expected = re.match(regex.email_regex_pattern, actual)
    assert expected is None


def test_should_identify_a_valid_cpf_with_points_returning_not_none(regex):
    actual: str = "041.326.650-89"
    expected = re.match(regex.cpf_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_cpf_with_points_returning_none(regex):
    actual: str = "041.326.650-8"
    expected = re.match(regex.cpf_regex_pattern, actual)
    assert expected is None


def test_should_identify_a_valid_cpf_without_points_returning_not_none(regex):
    actual: str = "04132665089"
    expected = re.match(regex.cpf_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_cpf_without_points_returning_none(regex):
    actual: str = "0413266508"
    expected = re.match(regex.cpf_regex_pattern, actual)
    assert expected is None


def test_should_identify_a_valid_cnpj_with_points_returning_not_none(regex):
    actual: str = "26.710.845/0001-64"
    expected = re.match(regex.cnpj_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_cnpj_with_points_returning_none(regex):
    actual: str = "26.710.845/0001-6"
    expected = re.match(regex.cnpj_regex_pattern, actual)
    assert expected is None


def test_should_identify_a_valid_cnpj_without_points_returning_not_none(regex):
    actual: str = "26710845000164"
    expected = re.match(regex.cnpj_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_cnpj_without_points_returning_none(regex):
    actual: str = "2671084500016"
    expected = re.match(regex.cnpj_regex_pattern, actual)
    assert expected is None


def test_should_identify_a_valid_url_returning_not_none(regex):
    actual: str = "https://www.any.com"
    expected = re.match(regex.url_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_url_returning_none(regex):
    actual: str = "any_text"
    expected = re.match(regex.url_regex_pattern, actual)
    assert expected is None


def test_should_identify_only_numbers_returning_not_none(regex):
    actual: str = "10000"
    expected = re.match(regex.only_number_regex_pattern, actual)
    assert expected is not None


def test_should_identify_only_numbers_returning_none(regex):
    actual: str = "AB01"
    expected = re.match(regex.only_number_regex_pattern, actual)
    assert expected is None


def test_should_identify_letters_and_numbers_returning_not_none(regex):
    actual: str = "AB01"
    expected = re.match(regex.only_letters_and_numbers_regex_pattern, actual)
    assert expected is not None


def test_should_identify_letters_and_numbers_returning_none(regex):
    actual: str = str()
    expected = re.match(regex.only_letters_and_numbers_regex_pattern, actual)
    assert expected is None


def test_should_identify_a_valid_passport_returning_not_none(regex):
    actual: str = "JM112035"
    expected = re.match(regex.passport_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_passport_returning_none(regex):
    actual: str = "any"
    expected = re.match(regex.passport_regex_pattern, actual)
    assert expected is not None
