from unittest import TestCase

from node.node import Node


class TestNode(TestCase):
    def test_is_int(self):
        self.assertTrue(Node('34').is_int())
        self.assertTrue(Node('3-4').is_int())
        self.assertTrue(Node('3%4').is_int())
        self.assertTrue(Node('-3%4').is_int())
        self.assertFalse(Node('-3a4').is_int())
        self.assertFalse(Node('node').is_int())

    def test_is_word(self):
        self.assertFalse(Node('34').is_word())
        self.assertTrue(Node('node').is_word())
        self.assertTrue(Node('no-de').is_word())
        self.assertTrue(Node('no$de').is_word())

    def test_value_string_returns_parsed_token(self):
        value_string = Node('333-#%4').value_string()
        self.assertEqual('3334', value_string)

        value_string = Node('w#3o5rd').value_string()
        self.assertEqual('word', value_string)

    def test_value_returns_appropriate_value(self):
        value_string = Node('333-#%4').value()
        self.assertEqual(3334, value_string)

        value_string = Node('w#3o5rd').value()
        self.assertEqual('word', value_string)

    def test_nodes_are_orderable(self):
        int1 = Node('3-#%3')
        int2 = Node('33-#%333')
        self.assertLess(int1, int2)

        word1 = Node('w$$ord')
        word2 = Node('3*45zebra')
        self.assertLess(word1, word2)

        self.assertRaises(ValueError, lambda: int1 < word2)
        self.assertRaises(ValueError, lambda: word2 < int1)
