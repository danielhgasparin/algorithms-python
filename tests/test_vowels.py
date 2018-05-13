import unittest
from algorithms.vowels import *

class TestVowels(unittest.TestCase):
    def test_vowels(self):
        self.assertEqual(vowels("A text with vowels."), 5)
        self.assertEqual(vowels("Why?"), 0)
    
    
    def test_vowels_loop(self):
        self.assertEqual(vowels_loop("A text with vowels."), 5)
        self.assertEqual(vowels_loop("Why"), 0)