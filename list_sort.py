from node import Node


class ListSort:
    def __init__(self, original_string):
        self._node_list = [Node(x) for x in original_string.split()]
        self._tag_list = [x.is_int() for x in self._node_list]
        self._word_list = sorted([x for x in self._node_list if x.is_word()])
        self._int_list = sorted([x for x in self._node_list if x.is_int()])

    def zip_sorted(self):
        return ' '.join([self._int_or_word(x) for x in self._tag_list])

    def _int_or_word(self, is_int_position):
        if is_int_position:
            return str(self._int_list.pop(0).value())
        else:
            return self._word_list.pop(0).value()
