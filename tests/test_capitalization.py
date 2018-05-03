import unittest
from algorithms.capitalization import *

class TestCapitalization(unittest.TestCase):
    def test_title_case(self):
        self.assertEqual(title_case("what's your favorite color?"), "What's Your Favorite Color?")

    def test_title_case_loop(self):
        self.assertEqual(title_case_loop("what's your favorite color?"), "What's Your Favorite Color?")