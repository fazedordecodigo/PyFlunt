"""Module Sample Entity."""
from flunt.notification import Notification


class SampleEntity(Notification):
    """Class Sample Entity."""

    def __init__(self) -> None:
        """Found 'Constructor'."""
        self.bool_false_property = False
        self.bool_true_property = True
        self.bool_none_property = None
