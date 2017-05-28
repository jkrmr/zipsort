import re


class Node:
    def __init__(self, str):
        self.__str = re.sub(r'[^0-9A-Za-z]', '', str)
        self.__is_int = not not re.match(r'[0-9]', str)

    def is_int(self):
        return self.__is_int

    def is_word(self):
        return not self.is_int()

    def value(self):
        if self.is_int():
            return int(self.__str)
        else:
            return self.__str

    def __lt__(self, other):
        return self.value().__lt__(other.value())

    def __eq__(self, other):
        return self.value().__eq__(other.value())
