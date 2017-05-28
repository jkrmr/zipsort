import re


class Node:
    """
    Wraps a string token, decides whether it's a word or an int,
    returns appropriate value via value().

    Implements __lt__ to be orderable.
    """

    def __init__(self, token):
        self._token = re.sub(r'[^0-9A-Za-z]', '', token)
        self._is_int = not not re.match(r'[0-9]', token)

    def is_int(self):
        """
        Returns: True if an int node. False otherwise.
        """
        return self._is_int

    def is_word(self):
        """
        Returns: True if a word node. False otherwise.
        """
        return not self.is_int()

    def value_string(self):
        """
        Returns: The tokenized input string.
        """
        return self._token

    def value(self):
        """
        Parses a stringified integer to an Int if an int node.
        Otherwise, just returns the string.

        Returns: A String if a word node, an Int if an int node.
        """
        if self.is_int():
            return int(self.value_string())
        else:
            return self.value_string()

    def __lt__(self, other):
        return self.value().__lt__(other.value())
