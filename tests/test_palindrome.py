import unittest
from algorithms.palindrome import *

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("aa"))
        self.assertTrue(is_palindrome("abba"))
        self.assertTrue(is_palindrome("abcba"))
        self.assertFalse(is_palindrome("ab"))
        self.assertFalse(is_palindrome("abab"))
        self.assertFalse(is_palindrome("abcza"))


    def test_is_palindrome_functional(self):
        self.assertTrue(is_palindrome_functional("a"))
        self.assertTrue(is_palindrome_functional("aa"))
        self.assertTrue(is_palindrome_functional("abba"))
        self.assertTrue(is_palindrome_functional("abcba"))
        self.assertFalse(is_palindrome_functional("ab"))
        self.assertFalse(is_palindrome_functional("abab"))
        self.assertFalse(is_palindrome_functional("abcza"))