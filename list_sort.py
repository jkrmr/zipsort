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


class ListSort:
    def __init__(self, original):
        self.__original = original
        self.__node_list = list(map(Node, original.split()))
        self.__tag_list = list(map(lambda x: x.is_int(), self.__node_list))
        self.__word_list = sorted([x for x in self.__node_list if x.is_word()])
        self.__int_list = sorted([x for x in self.__node_list if x.is_int()])

    def zip_sorted(self):
        zipped = []

        for int_pos in self.__tag_list:
            if int_pos:
                zipped.append(self.__int_list.pop(0).value())
            else:
                zipped.append(self.__word_list.pop(0).value())

        return ' '.join(str(x) for x in zipped)
