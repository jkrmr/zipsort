from node import Node


class ZipSort:
    def __init__(self, original_string):
        # tokenize the input string
        node_list = [Node(x) for x in original_string.split()]
        # create an associated list marking int / word positions
        self._tag_list = [x.is_int() for x in node_list]
        # filter and sort word and int nodes
        self._word_list = sorted([x for x in node_list if x.is_word()])
        self._int_list = sorted([x for x in node_list if x.is_int()])

    def zip_sorted(self):
        """
        "Zip" together sorted int and word values back into a list in the
        appropriate positions.
        """
        return ' '.join([self._int_or_word(x) for x in self._tag_list])

    def _int_or_word(self, is_int_position):
        """
        Pop a node off the front of the appropriate list and return its
        tokenized value string.
        """
        if is_int_position:
            appropriate_list = self._int_list
        else:
            appropriate_list = self._word_list

        return appropriate_list.pop(0).value_string()
