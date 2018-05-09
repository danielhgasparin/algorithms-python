"""Run this module to execute all tests.

Alternatively, run the unittest built-in module.

Usage:
    python tests_main.py
    python -m unittest 
    python -m unittest [<module>.<test-case>]
    python -m unittest [<module>.<test-case>[.<test-method>]]
"""

import unittest
import tests.test_fibonacci
import tests.test_reverse_string
import tests.test_palindrome
import tests.test_reverse_integer
import tests.test_max_occurrence
import tests.test_fizzbuzz
import tests.test_array_chunk
import tests.test_anagram
import tests.test_capitalization
import tests.test_steps
import tests.test_pyramid_steps
import tests.test_vowels
import tests.test_spiral_matrix
import tests.test_queue
import tests.test_weave
import tests.test_stack

loader = unittest.TestLoader()
suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=2)

suite.addTest(loader.loadTestsFromModule(tests.test_fibonacci))
suite.addTest(loader.loadTestsFromModule(tests.test_reverse_string))
suite.addTest(loader.loadTestsFromModule(tests.test_palindrome))
suite.addTest(loader.loadTestsFromModule(tests.test_reverse_integer))
suite.addTest(loader.loadTestsFromModule(tests.test_max_occurrence))
suite.addTest(loader.loadTestsFromModule(tests.test_fizzbuzz))
suite.addTest(loader.loadTestsFromModule(tests.test_array_chunk))
suite.addTest(loader.loadTestsFromModule(tests.test_anagram))
suite.addTest(loader.loadTestsFromModule(tests.test_capitalization))
suite.addTest(loader.loadTestsFromModule(tests.test_steps))
suite.addTest(loader.loadTestsFromModule(tests.test_pyramid_steps))
suite.addTest(loader.loadTestsFromModule(tests.test_vowels))
suite.addTest(loader.loadTestsFromModule(tests.test_spiral_matrix))
suite.addTest(loader.loadTestsFromModule(tests.test_queue))
suite.addTest(loader.loadTestsFromModule(tests.test_weave))
suite.addTest(loader.loadTestsFromModule(tests.test_stack))

runner.run(suite)