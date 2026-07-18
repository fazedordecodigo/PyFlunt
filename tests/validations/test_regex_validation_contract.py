from __future__ import annotations

import pytest

from flunt.validations.regex_validation_contract import (
    RegexValidationContract,
)


def test_should_be_valid_when_value_matches_pattern() -> None:
    contract = RegexValidationContract()
    contract.matches("hello@email.com", r".+@.+\..+", "Email")

    assert contract.is_valid


def test_should_be_invalid_when_value_does_not_match_pattern() -> None:
    contract = RegexValidationContract()
    contract.matches("invalid", r".+@.+\..+", "Email")

    assert contract.is_valid is False


def test_should_be_valid_when_value_does_not_match_not_matches() -> None:
    contract = RegexValidationContract()
    contract.not_matches("hello@email.com", r"^\d+$", "Email")

    assert contract.is_valid


def test_should_be_invalid_when_value_matches_not_matches() -> None:
    contract = RegexValidationContract()
    contract.not_matches("12345", r"^\d+$", "Numbers")

    assert contract.is_valid is False


def test_should_return_notification_with_default_message_when_matches_fails() -> (
    None
):
    contract = RegexValidationContract()
    contract.matches("abc", r"^\d+$", "Numbers")

    notification = contract.get_notifications()[0]
    assert notification.message == "The field Numbers must match the pattern ^\\d+$"


def test_should_return_notification_with_default_message_when_not_matches_fails() -> (
    None
):
    contract = RegexValidationContract()
    contract.not_matches("123", r"^\d+$", "Numbers")

    notification = contract.get_notifications()[0]
    assert (
        notification.message
        == "The field Numbers must not match the pattern ^\\d+$"
    )


def test_should_return_custom_message_when_matches_fails() -> None:
    contract = RegexValidationContract()
    contract.matches("abc", r"^\d+$", "Numbers", "Custom message")

    notification = contract.get_notifications()[0]
    assert notification.message == "Custom message"


def test_should_return_custom_message_when_not_matches_fails() -> None:
    contract = RegexValidationContract()
    contract.not_matches("123", r"^\d+$", "Numbers", "Custom message")

    notification = contract.get_notifications()[0]
    assert notification.message == "Custom message"


def test_should_be_valid_when_value_is_empty_string_and_matches() -> None:
    contract = RegexValidationContract()
    contract.matches("", r"^$", "Empty")

    assert contract.is_valid


def test_should_return_a_once_notification_when_matches_is_invalid() -> None:
    contract = RegexValidationContract()
    contract.matches("abc", r"^\d+$", "Numbers")

    assert len(contract.get_notifications()) == 1


def test_should_return_a_once_notification_when_not_matches_is_invalid() -> None:
    contract = RegexValidationContract()
    contract.not_matches("123", r"^\d+$", "Numbers")

    assert len(contract.get_notifications()) == 1
