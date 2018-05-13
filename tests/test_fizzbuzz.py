import unittest
from algorithms.fizzbuzz import *

class TestFizzbuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertListEqual(fizzbuzz(30), ["1", "2", "fizz", "4", "buzz", "fizz","7", "8", "fizz", "buzz", 
                                            "11", "fizz", "13", "14", "fizzbuzz", "16", "17", "fizz", "19", "buzz",
                                            "fizz", "22", "23", "fizz", "buzz", "26", "fizz", "28", "29", "fizzbuzz"])


    def test_run_fizzbuzz_generator(self):
        self.assertListEqual(run_fizzbuzz_generator(30), ["1", "2", "fizz", "4", "buzz", "fizz","7", "8", "fizz", "buzz", 
                                                          "11", "fizz", "13", "14", "fizzbuzz", "16", "17", "fizz", "19", "buzz",
                                                          "fizz", "22", "23", "fizz", "buzz", "26", "fizz", "28", "29", "fizzbuzz"])