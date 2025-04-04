"""Test for Notification class."""

from flunt.notifications.notification import Notification


class TestNotification:
    """Test cases for Notification class."""

    def test_init_notification(self) -> None:
        """Test initialization of Notification class."""
        notification = Notification(field="Nome", message="Nome é obrigatório")

        assert notification.field == "Nome"
        assert notification.message == "Nome é obrigatório"

    def test_str_representation(self) -> None:
        """Test the string representation of Notification."""
        notification = Notification(field="Email", message="Email inválido")

        assert str(notification) == "Email: Email inválido"

    def test_repr_representation(self) -> None:
        """Test the representation of Notification."""
        notification = Notification(
            field="Idade", message="Idade deve ser positiva"
        )

        assert repr(notification) == "Idade: Idade deve ser positiva"

    def test_notification_with_empty_field(self) -> None:
        """Test Notification with empty field."""
        notification = Notification(field="", message="Mensagem de erro")

        assert notification.field == ""
        assert notification.message == "Mensagem de erro"
        assert str(notification) == ": Mensagem de erro"

    def test_notification_with_empty_message(self) -> None:
        """Test Notification with empty message."""
        notification = Notification(field="Campo", message="")

        assert notification.field == "Campo"
        assert notification.message == ""
        assert str(notification) == "Campo: "

    def test_str_and_repr_are_equal(self) -> None:
        """Test that __str__ and __repr__ methods return the same value."""
        notification = Notification(
            field="Preço", message="Preço deve ser maior que zero"
        )

        assert str(notification) == repr(notification)

    def test_notification_with_special_characters(self) -> None:
        """Test Notification with special characters in the field and message."""
        notification = Notification(
            field="Código#1", message="Caracteres especiais: @!$%"
        )

        assert notification.field == "Código#1"
        assert notification.message == "Caracteres especiais: @!$%"
        assert str(notification) == "Código#1: Caracteres especiais: @!$%"
