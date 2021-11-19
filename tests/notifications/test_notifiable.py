"""Module Test Notifiable."""
from flunt.notification import Notification
from tests.models.vo import Name
import unittest


class NotifiableTests(unittest.TestCase):
    """Class Notifiable Test."""

    def setUp(self):
        """Execute Setup Test."""
        self._name = Name('Emerson', 'Delatorre')

    def test_deve_ser_true_instanciado_vo(self):
        """Test Is Valid."""
        self.assertTrue(self._name.is_valid())
