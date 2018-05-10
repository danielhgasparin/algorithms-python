import unittest
from algorithms.linked_list import *

class TestLinkedList(unittest.TestCase):
    def test_linked_list(self):
        linked = LinkedList()
        self.assertEqual(linked.size(), 0)
        self.assertEqual(linked.get_head(), None)
        self.assertEqual(linked.get_tail(), None)
        linked.remove_head()
        linked.remove_tail()
        linked.insert(1)
        linked.insert(2)
        linked.insert(3)
        linked.insert(4)
        self.assertEqual(linked.size(), 4)
        self.assertEqual(linked.get_head().value, 4)
        self.assertEqual(linked.get_tail().value, 1)
        linked.remove_head()
        self.assertEqual(linked.get_head().value, 3)
        linked.remove_tail()
        self.assertEqual(linked.get_tail().value, 2)
        linked.clear()
        self.assertEqual(linked.size(), 0)

    def test_linked_list_insert(self):
        linked = LinkedList()
        linked.insert(1)
        linked.insert(2)
        linked.insert(3)

    def test_linked_list_size(self):
        linked = LinkedList()
        self.assertEqual(linked.size(), 0)
        linked.insert(1)
        linked.insert(2)
        linked.insert(3)
        self.assertEqual(linked.size(), 3)

    def test_linked_list_get_head(self):
        linked = LinkedList()
        self.assertEqual(linked.get_head(), None)
        linked.insert(1)
        linked.insert(2)
        linked.insert(3)
        self.assertEqual(linked.get_head().value, 3)

    def test_linked_list_get_tail(self):
        linked = LinkedList()
        self.assertEqual(linked.get_tail(), None)
        linked.insert(1)
        linked.insert(2)
        linked.insert(3)
        self.assertEqual(linked.get_tail().value, 1)

    def test_linked_list_clear(self):
        linked = LinkedList()
        linked.clear()
        linked.insert(1)
        linked.insert(2)
        linked.insert(3)
        linked.clear()
        self.assertEqual(linked.size(), 0)

    def test_linked_list_remove_head(self):
        linked = LinkedList()
        linked.remove_head()
        linked.insert(1)
        linked.remove_head()
        self.assertEqual(linked.get_head(), None)
        linked.insert(1)
        linked.insert(2)
        linked.remove_head()
        self.assertEqual(linked.get_head().value, 1)
        linked.insert(3)
        linked.insert(4)
        linked.remove_head()
        self.assertEqual(linked.get_head().value, 3)

    def test_linked_list_remove_tail(self):
        linked = LinkedList()
        linked.remove_tail()
        linked.insert(1)
        linked.remove_tail()
        self.assertEqual(linked.get_tail(), None)
        linked.insert(1)
        linked.insert(2)
        linked.remove_tail()
        self.assertEqual(linked.get_tail().value, 2)
        linked.insert(3)
        linked.insert(4)
        linked.remove_tail()
        self.assertEqual(linked.get_tail().value, 3)

    def test_linked_list_insert_tail(self):
        linked = LinkedList()
        linked.insert_tail(1)
        self.assertEqual(linked.get_head().value, 1)
        linked.clear()
        linked.insert(1)
        linked.insert(2)
        linked.insert_tail(3)
        self.assertEqual(linked.get_tail().value, 3)