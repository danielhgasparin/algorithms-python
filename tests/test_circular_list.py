import unittest
from algorithms.linked_list import LinkedList
from algorithms.circular_list import *

class TestCircularList(unittest.TestCase):
    def test_circular_list(self):
        linked = LinkedList()
        self.assertFalse(is_circular(linked))
        linked.insert(1)
        self.assertFalse(is_circular(linked))
        linked.insert(2)
        self.assertFalse(is_circular(linked))
        linked.insert(3)
        self.assertFalse(is_circular(linked))
        linked.get_tail().next = linked.get_head()
        self.assertTrue(is_circular(linked))
        linked.get_at(2).next = linked.get_at(1)
        self.assertTrue(is_circular(linked))
        linked.get_head().next =  linked.get_head()
        self.assertTrue(is_circular(linked))