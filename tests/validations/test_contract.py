
from faker import Faker

from flunt.validations.contract import Contract


fake = Faker()

def should_be_valid_and_not_return_notification_when_required_is_not_none():
    contract = Contract().requires(None, "any_key", "any_message")
    assert contract.is_valid