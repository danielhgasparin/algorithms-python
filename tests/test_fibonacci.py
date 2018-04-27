import unittest
from algorithms.fibonacci import *

class TestFibonacci(unittest.TestCase):
    """Tests for the "fibonacci" module."""

    def setUp(self):
        """Preparation to be executed prior to all tests."""
        pass

    def tearDown(self):
        """Clean up to be executed after all tests."""
        pass

    def test_fib(self):
        self.assertListEqual(fib(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fib_up_to(self):
        self.assertListEqual(fib_up_to(100), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_run_fib_generator(self):
        self.assertListEqual(run_fib_generator(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fib_recursive(self):
        self.assertListEqual(fib_recursive(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fib_recursive_mathy(self):
        self.assertEqual(fib_recursive_mathy(0), 0)
        self.assertEqual(fib_recursive_mathy(10), 55)

    def test_run_fib_recursive_mathy(self):
        self.assertListEqual(run_fib_recursive_mathy(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])