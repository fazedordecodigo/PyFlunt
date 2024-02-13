"""Module Contract."""

from flunt.notifications.notifiable import Notifiable
from flunt.notifications.notification import Notification


class StringValidationContract(Notifiable):
    """
    Class for validating string values and adding notifications based on various comparisons.

    Parameters
    ----------
        N/A

    Attributes
    ----------
        N/A

    Methods
    -------
    - is_lower_than(value, comparer, key, message): Checks if the length of a string value is lower than a given number.
    - is_lower_or_equals_than(value, comparer, key, message): Checks if the length of a string value is lower or equal to a given number.
    - is_greater_than(value, comparer, key, message): Checks if the length of a string value is greater than a given number.
    - is_greater_or_equals_than(value, comparer, key, message): Checks if the length of a string value is greater or equal to a given number.
    - is_none(value, key, message): Checks if a string value is None.
    - is_not_none(value, key, message): Checks if a string value is not None.
    - is_not_none_or_white_space(value, key, message): Checks if a string value is not None or whitespace.
    - are_equals(value, comparer, key, message): Checks if two string values are equal.
    - are_not_equals(value, comparer, key, message): Checks if two string values are not equal.
    - contains(value, comparer, key, message): Checks if a string contains a specific substring.
    - not_contains(value, comparer, key, message): Checks if a string does not contain a specific substring.
    - is_between(value, min, max, key, message): Checks if the length of a string is between a minimum and maximum value.

    """

    def is_lower_than(self, value: str, comparer: int, key: str, message: str):
        """
        Check if the length of a string value is lower than a given number and adds a notification if it's greater.

        Parameters
        ----------
        `value`: str
            The string value to compare.
        `comparer`: int
            The maximum length allowed for the value.
        `key`: str
            The key or identifier associated with the comparison.
        `message`: str
            The notification message to be added if the length exceeds the comparer.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is an empty string or None, no notification is added.
        - If the length of `value` is greater than `comparer`, a notification is added to the current instance
        with the provided `key` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
              .is_lower_than("Hello", 10, "LengthCheck", "Value should have a length less than 10")
        obj.is_valid
        ```

        """
        if not value:
            return self

        if len(value) > comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_lower_or_equals_than(
        self, value: str, comparer: int, key: str, message: str
    ):
        """
        Check if the length of a string value is lower or equal to a given number and adds a notification if it exceeds.

        Parameters
        ----------
        `value`: str
            The string value to compare.
        `comparer`: int
            The maximum length allowed for the value.
        `key`: str
            The key or identifier associated with the comparison.
        `message`: str
            The notification message to be added if the length exceeds the comparer.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is an empty string or None, no notification is added.
        - If the length of `value` is greater than or equal to `comparer`, a notification is added to the current instance
        with the provided `key` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
              .is_lower_or_equals_than("Hello", 10, "LengthCheck", "Value should have a length less than or equal to 10")
        obj.is_valid
        ```

        """
        if not value:
            return self

        if len(value) >= comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_greater_than(self, value: str, comparer: int, key: str, message: str):
        """
        Check if the length of a string value is greater than a given number and adds a notification if it's smaller.

        Parameters
        ----------
        `value`: str
            The string value to compare.
        `comparer`: int
            The minimum length required for the value.
        `key`: str
            The key or identifier associated with the comparison.
        `message`: str
            The notification message to be added if the length is smaller than the comparer.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is an empty string or None, no notification is added.
        - If the length of `value` is smaller than `comparer`, a notification is added to the current instance
        with the provided `key` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
              .is_greater_than("Hello", 3, "LengthCheck", "Value should have a length greater than 3")
        obj.is_valid
        ```

        """
        if not value:
            return self

        if len(value) < comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_greater_or_equals_than(
        self, value: str, comparer: int, key: str, message: str
    ):
        """
        Check if the length of a string value is greater than or equal to a given number and adds a notification if it's smaller.

        Parameters
        ----------
        `value`: str
            The string value to compare.
        `comparer`: int
            The minimum length required for the value.
        `key`: str
            The key or identifier associated with the comparison.
        `message`: str
            The notification message to be added if the length is smaller than the comparer.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is an empty string or None, no notification is added.
        - If the length of `value` is smaller than or equal to `comparer`, a notification is added to the current instance
        with the provided `key` and `message`.

        Example
        --------
        ```python
        obj = Contract()
              .is_greater_or_equals_than("Hello", 3, "LengthCheck", "Value should have a length greater than or equal to 3")
        obj.is_valid
        ```

        """
        if not value:
            return self

        if len(value) <= comparer:
            self.add_notification(Notification(key, message))

        return self

    def is_none(self, value: str, key: str, message: str):
        """
        Check if a string value is not None and adds a notification if it is.

        Parameters
        ----------
        `value`: str
            The string value to be checked.
        `key`: str
            The key or identifier associated with the check.
        `message`: str
            The notification message to be added if the value is None.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is not None, no notification is added.
        - If the `value` is None, a notification is added to the current instance with the provided `key` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
              .is_none("Hello", "ValueCheck", "Value should not be None")
        obj.is_valid
        ```

        """
        if value is not None:
            self.add_notification(Notification(key, message))

        return self

    def is_not_none(self, value: str, key: str, message: str):
        """
        Check if a string value is not None and adds a notification if it is.

        Parameters
        ----------
        `value`: str
            The string value to be checked.
        `key`: str
            The key or identifier associated with the check.
        `message`: str
            The notification message to be added if the value is None.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is None, a notification is added to the current instance with the provided `key` and `message`.
        - If the `value` is not None, no notification is added.

        Examples
        --------
        ```python
        obj = Contract()
              .is_not_none("Hello", "ValueCheck", "Value should not be None")
        obj.is_valid
        ```

        """
        if value is None:
            self.add_notification(Notification(key, message))

        return self

    def is_not_none_or_white_space(self, value: str, key: str, message: str):
        """
        Check if a string value is not None or whitespace and adds a notification if it is.

        Parameters
        ----------
        `value`: str
            The string value to be checked.
        `key`: str
            The key or identifier associated with the check.
        `message`: str
            The notification message to be added if the value is None or whitespace.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is None or consists only of whitespace characters (spaces, tabs, newlines, etc.),
        a notification is added to the current instance with the provided `key` and `message`.
        - If the `value` is not None and contains at least one non-whitespace character, no notification is added.

        Examples
        --------
        ```python
        obj = Contract()
              .is_not_none_or_white_space("Hello", "ValueCheck", "Value should not be None or whitespace")
        obj.is_valid
        ```

        """
        if value is None or value.isspace():
            self.add_notification(Notification(key, message))

        return self

    def are_equals(self, value: str, comparer: str, key: str, message: str):
        """
        Check if two string values are equal and adds a notification if they are not equal.

        Parameters
        ----------
        `value`: str
            The first string value to compare.
        `comparer`: str
            The second string value to compare with the first value.
        `key`: str
            The key or identifier associated with the comparison.
        `message`: str
            The notification message to be added if the values are not equal.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is not equal to `comparer`, a notification is added to the current instance
        with the provided `key` and `message`. Otherwise, no notification is added.

        Examples
        --------
        ```python
        obj = Contract()
              .are_equals("Hello", "Hello", "Comparison", "Values should be equal")
        obj.is_valid
        ```

        """
        if value != comparer:
            self.add_notification(Notification(key, message))

        return self

    def are_not_equals(self, value: str, comparer: str, key: str, message: str):
        """
        Require two strings are not equals.

        Parameters
        ----------
        `value`: str
            The value to be compared.
        `comparer`: str
            The value to compare with `value`.
        `key`: str
            The key or identifier related to the comparison.
        `message`: str
            The notification message in case of equal values.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is equal to `comparer`, a notification is added to the current instance
        with the provided `key` and `message`. Otherwise, no notification is added.

        Examples
        --------
        ```python
        obj = Contract()
              .are_not_equals("Hello", "World", "Comparison", "Values should not be equal")
        obj.is_valid
        ```

        """
        if value == comparer:
            self.add_notification(Notification(key, message))

        return self

    def contains(self, value: str, comparer: str, key: str, message: str):
        """
        Check if a string value contains another string and adds a notification if it does.

        Parameters
        ----------
        `value`: str
            The string value to be checked.
        `comparer`: str
            The string to search for within the value.
        `key`: str
            The key or identifier associated with the check.
        `message`: str
            The notification message to be added if the value contains the comparer.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` contains the `comparer` string, a notification is added to the current instance
        with the provided `key` and `message`.
        - If the `value` does not contain the `comparer` string, no notification is added.

        Examples
        --------
        ```python
        obj = Contract()
              .contains("Hello, world!", "world", "ContainsCheck", "Value should contain 'world'")
        obj.is_valid
        ```

        """
        if value.find(comparer) > -1:
            self.add_notification(Notification(key, message))

        return self

    def not_contains(self, value: str, comparer: str, key: str, message: str):
        """
        Check if a string value does not contain a specified substring and adds a notification if it does.

        Parameters
        ----------
        `value`: str
            The string value to be checked.
        `comparer`: str
            The substring to search for in the value.
        `key`: str
            The key or identifier associated with the check.
        `message`: str
            The notification message to be added if the value contains the comparer.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` does not contain the `comparer` substring, no notification is added.
        - If the `value` contains the `comparer` substring, a notification is added to the current instance
        with the provided `key` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
              .not_contains("Hello", "World", "Comparison", "Value should not contain 'World'")
        obj.is_valid
        ```

        """
        if value.find(comparer) == -1:
            self.add_notification(Notification(key, message))

        return self

    def is_between(self, value: str, min: int, max: int, key: str, message: str):
        """
        Require a string value to have a length between a minimum and maximum value (inclusive), and adds a notification if the length is outside the specified range.

        Parameters
        ----------
        `value`: str
            The string value to be checked.
        `min`: int
            The minimum allowed length for the value.
        `max`: int
            The maximum allowed length for the value.
        `key`: str
            The key or identifier associated with the length check.
        `message`: str
            The notification message to be added if the length is outside the range.

        Returns
        -------
        `self`
            The current instance with potential notifications added.

        Notes
        -----
        - If the `value` is empty, the function returns the current instance without adding any notifications.
        - If the `value` is None or consists only of whitespace characters, the function returns the current instance without adding any notifications.
        - If the length of `value` is less than `min` or greater than `max`, a notification is added to the current instance
        with the provided `key` and `message`.

        Examples
        --------
        ```python
        obj = Contract()
              .is_between("Hello", 3, 6, "LengthCheck", "Value length should be between 3 and 6")
        obj.is_valid
        ```

        """
        if not value:
            return self

        if value is None or value.isspace():
            return self

        if len(value) < min or len(value) > max:
            self.add_notification(Notification(key, message))

        return self
