import re


def test_should_identify_a_valid_email_address_returning_not_none(regex):
    actual = "any@any.com"
    expected = re.match(regex.email_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_email_address_returning_none(regex):
    actual = "any.com"
    expected = re.match(regex.email_regex_pattern, actual)
    assert expected is None


def test_should_identify_a_valid_cpf_with_points_returning_not_none(regex):
    actual = "041.326.650-89"
    expected = re.match(regex.cpf_cnpj_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_cpf_with_points_returning_none(regex):
    actual = "041.326.650-8"
    expected = re.match(regex.cpf_cnpj_regex_pattern, actual)
    assert expected is None


def test_should_identify_a_valid_cpf_without_points_returning_not_none(regex):
    actual = "04132665089"
    expected = re.match(regex.cpf_cnpj_regex_pattern, actual)
    assert expected is not None


def test_should_identify_a_invalid_cpf_without_points_returning_none(regex):
    actual = "0413266508"
    expected = re.match(regex.cpf_cnpj_regex_pattern, actual)
    assert expected is None
