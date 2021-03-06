import unittest
from algorithms.linked_list import LinkedList

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


    def test_linked_list_get_at(self):
        linked = LinkedList()
        self.assertEqual(linked.get_at(0), None)
        linked.insert(1)
        linked.insert(2)
        linked.insert(3)
        self.assertEqual(linked.get_at(0).value, 3)
        self.assertEqual(linked.get_at(2).value, 1)
        self.assertEqual(linked.get_at(10), None)


    def test_linked_list_remove_at(self):
        linked = LinkedList()
        linked.remove_at(0)
        linked.insert(1)
        linked.remove_at(0)
        self.assertEqual(linked.get_at(0), None)
        linked.insert(1)
        linked.insert(2)
        linked.insert(3)
        linked.remove_at(1)
        self.assertEqual(linked.get_at(1).value, 1)
        linked.remove_at(1)
        self.assertEqual(linked.get_at(1), None)
        linked.remove_at(1)
        self.assertEqual(linked.get_at(0).value, 3)
        linked.remove_at(10)
        self.assertEqual(linked.get_at(0).value, 3)


    def test_linked_list_insert_at(self):
        linked = LinkedList()
        linked.insert_at(0, 1)
        self.assertEqual(linked.get_at(0).value, 1)
        linked.clear()
        linked.insert_at(10, 1)
        self.assertEqual(linked.get_at(0).value, 1)
        linked.clear()
        linked.insert(1)
        linked.insert(2)
        linked.insert(3)
        linked.insert_at(1, 4)
        self.assertEqual(linked.get_at(1).value, 4)
        self.assertEqual(linked.get_at(2).value, 2)
        linked.insert_at(4, 5)
        self.assertEqual(linked.get_at(4).value, 5)
        linked.insert_at(10, 6)
        self.assertEqual(linked.get_at(5).value, 6)
        linked.insert_at(0, 7)
        self.assertEqual(linked.get_at(0).value, 7)


    def test_linked_list_iteration(self):
        linked = LinkedList()
        linked.insert(2)
        linked.insert(1)
        linked.insert(0)
        for i, node in enumerate(linked):
            self.assertEqual(node.value, i)
        self.assertListEqual(list(node.value for node in linked), [0, 1, 2])