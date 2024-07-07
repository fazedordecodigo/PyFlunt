"""Module Contract."""
from typing_extensions import Self

from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification
from flunt.localization import flunt_error_messages, flunt_regex_patterns
from flunt.validations import contract
import re

class UrlValidationContract(Notifiable):
    """
    Class to validate URL strings.

    This class provides methods for validating URL strings and adding notifications based on the validation results.

    Methods:
    -------
    is_url(value: str, key: str, message: str) -> Self:
        Checks if the provided string is a URL and adds a notification if it is not.
    
    is_url_or_empty(value: str, key: str, message: str) -> Self:
        Checks if the provided string is a URL or empty and adds a notification if it is not.
    
    is_not_url(value: str, key: str, message: str) -> Self:
        Checks if the provided string is not a URL and adds a notification if it is.
    
    is_not_url_or_empty(value: str, key: str, message: str) -> Self:
        Checks if the provided string is not a URL or empty and adds a notification if it is.
    """

    def is_url(self, value: str, key: str, message: str) -> Self:
        """
        Checks if the provided string is a URL.

        Parameters:
        ----------
        - value: str
            The string to be validated.
        - key: str
            The key to be used in the notification.
        - message: str
            The message to be used in the notification.

        Returns:
        -------
        - Self
            The instance of the class with the notification added if the validation fails.
        """
        if not re.match(flunt_regex_patterns.REGEX_URL, value):
            self.add_notification(Notification(key, message))
        return self
    
    def is_url_or_empty(self, value: str, key: str, message: str) -> Self:
        """
        Checks if the provided string is a URL or empty.

        Parameters:
        ----------
        - value: str
            The string to be validated.
        - key: str
            The key to be used in the notification.
        - message: str
            The message to be used in the notification.

        Returns:
        -------
        - Self
            The instance of the class with the notification added if the validation fails.
        """
        if value:
            if not re.match(flunt_regex_patterns.REGEX_URL, value):
                self.add_notification(Notification(key, message))
        return self
    
    def is_not_url(self, value: str, key: str, message: str) -> Self:
        """
        Checks if the provided string is not a URL.

        Parameters:
        ----------
        - value: str
            The string to be validated.
        - key: str
            The key to be used in the notification.
        - message: str
            The message to be used in the notification.

        Returns:
        -------
        - Self
            The instance of the class with the notification added if the validation fails.
        """
        if re.match(flunt_regex_patterns.REGEX_URL, value):
            self.add_notification(Notification(key, message))
        return self
    
    def is_not_url_or_empty(self, value: str, key: str, message: str) -> Self:
        """
        Checks if the provided string is not a URL or empty.

        Parameters:
        ----------
        - value: str
            The string to be validated.
        - key: str
            The key to be used in the notification.
        - message: str
            The message to be used in the notification.

        Returns:
        -------
        - Self
            The instance of the class with the notification added if the validation fails.
        """
        if value:
            if re.match(flunt_regex_patterns.REGEX_URL, value):
                self.add_notification(Notification(key, message))
        return self
    
    def is_url_nomsg(self, value: str, key: str) -> Self:
        """
        Checks if the provided string is a URL.

        Parameters:
        ----------
        - value: str
            The string to be validated.
        - key: str
            The key to be used in the notification.

        Returns:
        -------
        - Self
            The instance of the class with the notification added if the validation fails.
        """
        return self.is_url(value, key, flunt_error_messages.IS_URL_ERROR_MESSAGE(key))
    
    def is_url_or_empty_nomsg(self, value: str, key: str) -> Self:
        """
        Checks if the provided string is a URL or empty.

        Parameters:
        ----------
        - value: str
            The string to be validated.
        - key: str
            The key to be used in the notification.

        Returns:
        -------
        - Self
            The instance of the class with the notification added if the validation fails.
        """
        return self.is_url_or_empty(value, key, flunt_error_messages.IS_URL_OR_EMPTY_ERROR_MESSAGE(key))
    
    def is_not_url_nomsg(self, value: str, key: str) -> Self:
        """
        Checks if the provided string is not a URL.

        Parameters:
        ----------
        - value: str
            The string to be validated.
        - key: str
            The key to be used in the notification.

        Returns:
        -------
        - Self
            The instance of the class with the notification added if the validation fails.
        """
        return self.is_not_url(value, key, flunt_error_messages.IS_NOT_URL_ERROR_MESSAGE(key))
    
    def is_not_url_or_empty_nomsg(self, value: str, key: str) -> Self:
        """
        Checks if the provided string is not a URL or empty.

        Parameters:
        ----------
        - value: str
            The string to be validated.
        - key: str
            The key to be used in the notification.

        Returns:
        -------
        - Self
            The instance of the class with the notification added if the validation fails.
        """
        return self.is_not_url_or_empty(value, key, flunt_error_messages.IS_NOT_URL_OR_EMPTY_ERROR_MESSAGE(key))
