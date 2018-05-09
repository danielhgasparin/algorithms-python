import unittest
from algorithms.stack import *

class TestStack(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.peek(), None)
        with self.assertRaises(IndexError):
            stack.pop()