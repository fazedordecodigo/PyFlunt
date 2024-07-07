import pytest
from faker import Faker
from flunt.notifications.notification import Notification
from flunt.validations.url_validation_contract import UrlValidationContract

fake = Faker()

@pytest.mark.parametrize(
    'url, is_valid',
    [
        (fake.url(), True),
        ('http://example.com', True),
        ('https://example.com', True),
        ('ftp://example.com', True),
        ('invalid_url', False),
        ('www.example.com', False),
        ('', False),
        (None, False),
    ],
)
def test_is_url(url, is_valid):
    contract = UrlValidationContract()
    contract.is_url(url, 'url', 'Invalid URL')
    assert contract.is_valid == is_valid

@pytest.mark.parametrize(
    'url, is_valid',
    [
        (fake.url(), True),
        ('http://example.com', True),
        ('https://example.com', True),
        ('ftp://example.com', True),
        ('invalid_url', False),
        ('www.example.com', False),
        ('', True),
        (None, True),
    ],
)
def test_is_url_or_empty(url, is_valid):
    contract = UrlValidationContract()
    contract.is_url_or_empty(url, 'url', 'Invalid URL')
    assert contract.is_valid == is_valid

@pytest.mark.parametrize(
    'url, is_valid',
    [
        (fake.url(), False),
        ('http://example.com', False),
        ('https://example.com', False),
        ('ftp://example.com', False),
        ('invalid_url', True),
        ('www.example.com', True),
        ('', True),
        (None, True),
    ],
)
def test_is_not_url(url, is_valid):
    contract = UrlValidationContract()
    contract.is_not_url(url, 'url', 'Should not be a URL')
    assert contract.is_valid == is_valid

@pytest.mark.parametrize(
    'url, is_valid',
    [
        (fake.url(), False),
        ('http://example.com', False),
        ('https://example.com', False),
        ('ftp://example.com', False),
        ('invalid_url', True),
        ('www.example.com', True),
        ('', True),
        (None, True),
    ],
)
def test_is_not_url_or_empty(url, is_valid):
    contract = UrlValidationContract()
    contract.is_not_url_or_empty(url, 'url', 'Should not be a URL or should be empty')
    assert contract.is_valid == is_valid

def test_is_url_nomsg():
    contract = UrlValidationContract()
    valid_url = 'http://example.com'
    invalid_url = 'invalid_url'
    contract.is_url_nomsg(valid_url, 'url')
    assert contract.is_valid

    contract = UrlValidationContract()
    contract.is_url_nomsg(invalid_url, 'url')
    assert not contract.is_valid

def test_is_url_or_empty_nomsg():
    contract = UrlValidationContract()
    valid_url = 'http://example.com'
    invalid_url = 'invalid_url'
    empty_value = ''
    contract.is_url_or_empty_nomsg(valid_url, 'url')
    assert contract.is_valid

    contract = UrlValidationContract()
    contract.is_url_or_empty_nomsg(invalid_url, 'url')
    assert not contract.is_valid

    contract = UrlValidationContract()
    contract.is_url_or_empty_nomsg(empty_value, 'url')
    assert contract.is_valid

def test_is_not_url_nomsg():
    contract = UrlValidationContract()
    valid_url = 'http://example.com'
    invalid_url = 'invalid_url'
    contract.is_not_url_nomsg(valid_url, 'url')
    assert not contract.is_valid

    contract = UrlValidationContract()
    contract.is_not_url_nomsg(invalid_url, 'url')
    assert contract.is_valid

def test_is_not_url_or_empty_nomsg():
    contract = UrlValidationContract()
    valid_url = 'http://example.com'
    invalid_url = 'invalid_url'
    empty_value = ''
    contract.is_not_url_or_empty_nomsg(valid_url, 'url')
    assert not contract.is_valid

    contract = UrlValidationContract()
    contract.is_not_url_or_empty_nomsg(invalid_url, 'url')
    assert contract.is_valid

    contract = UrlValidationContract()
    contract.is_not_url_or_empty_nomsg(empty_value, 'url')
    assert contract.is_valid
