import re


class Node:
    """
    Wraps a string token, decides whether it's a word or an int,
    returns appropriate value via value().

    Implements __lt__ to be orderable.
    """

    def __init__(self, token):
        word_string = ''.join(re.findall(r'[A-Za-z]', token))
        number_string = ''.join(re.findall(r'[\-0-9]', token))
        self._is_int = not word_string

        if self.is_word():
            self._token = word_string
        else:
            is_nonnegative = number_string[0] != '-'
            number = re.sub(r'[^0-9]', '', number_string)
            complete_number = number if is_nonnegative else '-' + number
            self._token = complete_number

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
