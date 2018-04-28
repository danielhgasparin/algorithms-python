import unittest
from algorithms.reverse_integer import *

class TestReverseInteger(unittest.TestCase):
    def test_reverse_slice(self):
        self.assertEqual(reverse_slice(1234), 4321)
        self.assertEqual(reverse_slice(900), 9)
        self.assertEqual(reverse_slice(0), 0)
        self.assertEqual(reverse_slice(-1234), -4321)
        self.assertEqual(reverse_slice(-900), -9)