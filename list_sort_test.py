from unittest import TestCase

from list_sort import ListSort


class TestListSort(TestCase):
    def test_sorts_correctly(self):
        input = 'ba!!ker 55 c 5 a f d 1%0 h e 1'
        expected_output = 'a 1 baker 5 c d e 10 f h 55'

        result = ListSort(input).zip_sorted()

        self.assertEqual(expected_output, result)
