"""Module Sample Entity."""
from faker import Faker
from flunt.notifications.notification import Notification


class SampleEntity(Notification):
    """Class Sample Entity."""

    def __init__(self) -> None:
        """Found 'Constructor'."""
        fake = Faker()
        self.bool_false_property = False
        self.bool_true_property = True
        self.bool_none_property = None
        self.email_valid = fake.email()
        self.email_invalid = "any"
        self.first_name = "any_first_name"
        self.last_name = "any_last_name"
        self.credit_card_valid = fake.credit_card_number(card_type='amex')
        self.credit_card_invalid = "1234567890123456"
