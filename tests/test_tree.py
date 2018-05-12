import unittest
from algorithms.tree import Tree, Node

class TestTree(unittest.TestCase):
    def test_tree_traverse_breadth_first(self):
        
        def make_node_counter():
            count = 1
            def node_counter(node):
                nonlocal count
                node.value = str(count) + "_" + str(node.value)
                count += 1
            return node_counter
        
        tree = Tree()
        tree.root = Node(1)
        tree.root.add(2)
        tree.root.add(3)
        tree.root.add(4)
        tree.root.children[0].add(5)
        tree.root.children[0].add(6)
        tree.root.children[2].add(7)

        tree.traverse_breadth_first(make_node_counter())

        self.assertEqual(tree.root.value, "1_1")
        self.assertEqual(tree.root.children[0].value, "2_2")
        self.assertEqual(tree.root.children[1].value, "3_3")
        self.assertEqual(tree.root.children[2].value, "4_4")
        self.assertEqual(tree.root.children[0].children[0].value, "5_5")
        self.assertEqual(tree.root.children[0].children[1].value, "6_6")
        self.assertEqual(tree.root.children[2].children[0].value, "7_7")

    def test_tree_traverse_depth_first(self):
        
        def make_node_counter():
            count = 1
            def node_counter(node):
                nonlocal count
                node.value = str(count) + "_" + str(node.value)
                count += 1
            return node_counter
        
        tree = Tree()
        tree.root = Node(1)
        tree.root.add(2)
        tree.root.add(3)
        tree.root.add(4)
        tree.root.children[0].add(5)
        tree.root.children[0].add(6)
        tree.root.children[2].add(7)

        tree.traverse_depth_first(make_node_counter())

        self.assertEqual(tree.root.value, "1_1")
        self.assertEqual(tree.root.children[0].value, "2_2")
        self.assertEqual(tree.root.children[1].value, "5_3")
        self.assertEqual(tree.root.children[2].value, "6_4")
        self.assertEqual(tree.root.children[0].children[0].value, "3_5")
        self.assertEqual(tree.root.children[0].children[1].value, "4_6")
        self.assertEqual(tree.root.children[2].children[0].value, "7_7")