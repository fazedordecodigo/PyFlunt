import re

def test_should_identify_a_valid_email_address_returning_not_none(regex):
    actual = 'any@any.com'
    expected = re.match(regex.email_regex_pattern, actual)
    assert expected is not None

def test_should_identify_a_invalid_email_address_returning_none(regex):
    actual = 'any.com'
    expected = re.match(regex.email_regex_pattern, actual)
    assert expected is None