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
        self.assertListEqual(fib(0), [])
        self.assertListEqual(fib(1), [1])
        self.assertListEqual(fib(2), [1, 1])
        self.assertListEqual(fib(3), [1, 1, 2])
        self.assertListEqual(fib(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fib_up_to(self):
        self.assertListEqual(fib_up_to(0), [])
        self.assertListEqual(fib_up_to(1), [1, 1])
        self.assertListEqual(fib_up_to(2), [1, 1, 2])
        self.assertListEqual(fib_up_to(100), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_run_fib_generator(self):
        self.assertListEqual(run_fib_generator(0), [])
        self.assertListEqual(run_fib_generator(1), [1])
        self.assertListEqual(run_fib_generator(2), [1, 1])
        self.assertListEqual(run_fib_generator(3), [1, 1, 2])
        self.assertListEqual(run_fib_generator(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fib_recursive(self):
        self.assertListEqual(fib_recursive(0), [])
        self.assertListEqual(fib_recursive(1), [1])
        self.assertListEqual(fib_recursive(2), [1, 1])
        self.assertListEqual(fib_recursive(3), [1, 1, 2])
        self.assertListEqual(fib_recursive(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fib_recursive_mathy(self):
        self.assertEqual(fib_recursive_mathy(0), 0)
        self.assertEqual(fib_recursive_mathy(1), 1)
        self.assertEqual(fib_recursive_mathy(2), 1)
        self.assertEqual(fib_recursive_mathy(3), 2)
        self.assertEqual(fib_recursive_mathy(10), 55)

    def test_run_fib_recursive_mathy(self):
        self.assertListEqual(run_fib_recursive_mathy(0), [])
        self.assertListEqual(run_fib_recursive_mathy(1), [1])
        self.assertListEqual(run_fib_recursive_mathy(2), [1, 1])
        self.assertListEqual(run_fib_recursive_mathy(3), [1, 1, 2])
        self.assertListEqual(run_fib_recursive_mathy(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_run_fib_recursive_mathy_memoized(self):
        self.assertListEqual(run_fib_recursive_mathy_memoized(0), [])
        self.assertListEqual(run_fib_recursive_mathy_memoized(1), [1])
        self.assertListEqual(run_fib_recursive_mathy_memoized(2), [1, 1])
        self.assertListEqual(run_fib_recursive_mathy_memoized(3), [1, 1, 2])
        self.assertListEqual(run_fib_recursive_mathy_memoized(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    
    def test_run_fib_recursive_mathy_cached(self):
        self.assertListEqual(run_fib_recursive_mathy_cached(0), [])
        self.assertListEqual(run_fib_recursive_mathy_cached(1), [1])
        self.assertListEqual(run_fib_recursive_mathy_cached(2), [1, 1])
        self.assertListEqual(run_fib_recursive_mathy_cached(3), [1, 1, 2])
        self.assertListEqual(run_fib_recursive_mathy_cached(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])