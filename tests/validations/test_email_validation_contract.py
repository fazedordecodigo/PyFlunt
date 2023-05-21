
from tests.mocks.value_objects.vo import Email


def test_should_be_valid_when_correct_email():
    email = Email("any@any.com")
    assert email.is_valid()


def test_should_be_invalid_when_incorrect_email():
    email = Email("any")
    assert email.is_valid() is False
