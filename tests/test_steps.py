import unittest
from algorithms.steps import *

class TestSteps(unittest.TestCase):
    def test_steps_just(self):
        self.assertListEqual(steps_just(1), ["#"])
        self.assertListEqual(steps_just(2), ["# ", "##"])
        self.assertListEqual(steps_just(3), ["#  ", "## ", "###"])


    def test_steps_concat(self):
        self.assertListEqual(steps_concat(1), ["#"])
        self.assertListEqual(steps_concat(2), ["# ", "##"])
        self.assertListEqual(steps_concat(3), ["#  ", "## ", "###"])


    def test_steps_loop(self):
        self.assertListEqual(steps_loop(1), ["#"])
        self.assertListEqual(steps_loop(2), ["# ", "##"])
        self.assertListEqual(steps_loop(3), ["#  ", "## ", "###"])


    def test_steps_recursive(self):
        self.assertListEqual(steps_recursive(1), ["#"])
        self.assertListEqual(steps_recursive(2), ["# ", "##"])
        self.assertListEqual(steps_recursive(3), ["#  ", "## ", "###"])