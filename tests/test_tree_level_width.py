import unittest
from algorithms.tree import Tree, Node
from algorithms.tree_level_width import *

class TestTreeLevelWidth(unittest.TestCase):
    def test_tree_level_width(self):
        tree = Tree()
        tree.root = Node(1)
        tree.root.add(2)
        tree.root.add(3)
        tree.root.add(4)
        tree.root.children[0].add(5)
        tree.root.children[0].add(6)
        tree.root.children[0].add(7)
        tree.root.children[2].add(8)

        self.assertLessEqual(tree_level_width(tree), [1, 3, 4])