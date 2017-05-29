from unittest import TestCase

from zipsort.zipsort import ZipSort


class TestZipSort(TestCase):
    def test_handles_empty_input(self):
        result = ZipSort('').zip_sorted()
        self.assertEqual('', result)

    def test_sorts_simple_cases_correctly(self):
        input = 'ba!!ker 55 c 5 a f d 1%0 h e 1'
        expected_output = 'a 1 baker 5 c d e 10 f h 55'

        result = ZipSort(input).zip_sorted()

        self.assertEqual(expected_output, result)

    def test_sorts_uppercased_strings_correctly(self):
        input = 'Ba!!ker 55 c 5 a f d 1%0 h e 1'
        expected_output = 'Baker 1 a 5 c d e 10 f h 55'

        result = ZipSort(input).zip_sorted()

        self.assertEqual(expected_output, result)

    def test_sorts_negative_numbers_correctly(self):
        input = 'ba!!ke-r 5-5 c 5 a f d -1%0 h e -1'
        expected_output = 'a -10 baker -1 c d e 5 f h 55'

        result = ZipSort(input).zip_sorted()

        self.assertEqual(expected_output, result)
