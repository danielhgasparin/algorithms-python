import unittest
from algorithms.linked_list import LinkedList
from algorithms.linked_list_midnode import *

class TestLinkedListMidnode(unittest.TestCase):
    def test_linked_list_midnode(self):
        linked = LinkedList()
        self.assertEqual(midnode(linked), None)
        linked.insert(1)
        self.assertEqual(midnode(linked).value, 1)
        linked.insert(2)
        self.assertEqual(midnode(linked).value, 2)
        linked.insert(3)
        self.assertEqual(midnode(linked).value, 2)
        linked.insert(4)
        self.assertEqual(midnode(linked).value, 3)
        linked.insert(5)
        self.assertEqual(midnode(linked).value, 3)
        linked.insert(6)
        self.assertEqual(midnode(linked).value, 4)