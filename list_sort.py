from node import Node


class ListSort:
    def __init__(self, original_string):
        self.__node_list = [Node(x) for x in original_string.split()]
        self.__tag_list = [x.is_int() for x in self.__node_list]
        self.__word_list = sorted([x for x in self.__node_list if x.is_word()])
        self.__int_list = sorted([x for x in self.__node_list if x.is_int()])

    def zip_sorted(self):
        return ' '.join([self.__int_or_word(x) for x in self.__tag_list])

    def __int_or_word(self, is_int_position):
        if is_int_position:
            return str(self.__int_list.pop(0).value())
        else:
            return self.__word_list.pop(0).value()
