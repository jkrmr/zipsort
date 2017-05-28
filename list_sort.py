from node import Node


class ListSort:
    def __init__(self, original_string):
        self.__node_list = [Node(x) for x in original_string.split()]
        self.__tag_list = [x.is_int() for x in self.__node_list]
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
