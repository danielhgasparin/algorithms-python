import unittest
from algorithms.reverse_string import *

class TestReverseString(unittest.TestCase):
    def test_reverse_slice(self):
        self.assertEqual(reverse_slice("qwerty"), "ytrewq")

    def test_reverse_functional(self):
        self.assertEqual(reverse_functional("qwerty"), "ytrewq")

    def test_reverse_builtin(self):
        self.assertEqual(reverse_builtin("qwerty"), "ytrewq")

    def test_reverse_loop(self):
        self.assertEqual(reverse_loop("qwerty"), "ytrewq")