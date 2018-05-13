import unittest
from algorithms.anagram import *

class TestAnagram(unittest.TestCase):
    def test_anagram_sort(self):
        self.assertTrue(anagram_sort("rail safety", "fairy tales"))
        self.assertTrue(anagram_sort("Rail Safety 123!!!", "321fairytales"))
        self.assertFalse(anagram_sort("sea", "tea"))
        self.assertFalse(anagram_sort("apple", "apples"))
    

    def test_anagram_sort_regex(self):
        self.assertTrue(anagram_sort_regex("rail safety", "fairy tales"))
        self.assertTrue(anagram_sort_regex("Rail Safety 123!!!", "321fairytales"))
        self.assertFalse(anagram_sort_regex("sea", "tea"))
        self.assertFalse(anagram_sort_regex("apple", "apples"))
    

    def test_anagram_dict(self):
        self.assertTrue(anagram_dict("rail safety", "fairy tales"))
        self.assertTrue(anagram_dict("Rail Safety 123!!!", "321fairytales"))
        self.assertFalse(anagram_dict("sea", "tea"))
        self.assertFalse(anagram_dict("apple", "apples"))


    def test_anagram_dict_loop(self):
        self.assertTrue(anagram_dict_loop("rail safety", "fairy tales"))
        self.assertTrue(anagram_dict_loop("Rail Safety 123!!!", "321fairytales"))
        self.assertFalse(anagram_dict_loop("sea", "tea"))
        self.assertFalse(anagram_dict_loop("apple", "apples"))