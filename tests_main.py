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

loader = unittest.TestLoader()
suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=2)

suite.addTest(loader.loadTestsFromModule(tests.test_fibonacci))
suite.addTest(loader.loadTestsFromModule(tests.test_reverse_string))
suite.addTest(loader.loadTestsFromModule(tests.test_palindrome))
suite.addTest(loader.loadTestsFromModule(tests.test_reverse_integer))

runner.run(suite)