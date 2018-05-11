import unittest
from algorithms.linked_list import LinkedList
from algorithms.linked_list_from_tail import *

class TestLinkedListFromTail(unittest.TestCase):
    def test_linked_list_from_tail(self):
        linked = LinkedList()
        self.assertEqual(get_from_tail(linked, 0), None)
        linked.insert(1)
        self.assertEqual(get_from_tail(linked, 0).value, 1)
        linked.insert(2)
        linked.insert(3)
        self.assertEqual(get_from_tail(linked, 0).value, 1)
        self.assertEqual(get_from_tail(linked, 2).value, 3)
        self.assertEqual(get_from_tail(linked, 10), None)