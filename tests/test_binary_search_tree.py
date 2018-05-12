import unittest
from algorithms.binary_search_tree import Node

class TestBinarySearchTree(unittest.TestCase):
    def test_binary_search_tree_insert(self):
        root = Node(10)
        root.insert(1)
        root.insert(-1)
        root.insert(5)
        root.insert(20)
        root.insert(11)
        self.assertEqual(root.value, 10)
        self.assertEqual(root.left.value, 1)
        self.assertEqual(root.left.left.value, -1)
        self.assertEqual(root.left.right.value, 5)
        self.assertEqual(root.right.value, 20)
        self.assertEqual(root.right.left.value, 11)

    def test_binary_search_tree_contains(self):
        root = Node(10)
        root.insert(1)
        root.insert(-1)
        root.insert(5)
        root.insert(20)
        root.insert(11)
        self.assertEqual(root.contains(10).value, 10)
        self.assertEqual(root.contains(1).value, 1)
        self.assertEqual(root.contains(11).value, 11)
        self.assertEqual(root.contains(-2), None)
        self.assertEqual(root.contains(12), None)