import unittest
from algorithms.max_occurrence import *

class TestMaxOccurrence(unittest.TestCase):
    def test_max_occurrence(self):
        self.assertEqual(max_occurrence("Hello world"), "l")

    def test_max_occurrence_loop(self):
        self.assertEqual(max_occurrence_loop("Hello world"), "l")