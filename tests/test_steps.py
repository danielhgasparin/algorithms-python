import unittest
from algorithms.steps import *

class TestSteps(unittest.TestCase):
    def test_steps_just(self):
        self.assertListEqual(steps_just(4), ["#   ", "##  ", "### ", "####"])

    def test_steps_concat(self):
        self.assertListEqual(steps_concat(4), ["#   ", "##  ", "### ", "####"])

    def test_steps_loop(self):
        self.assertListEqual(steps_loop(4), ["#   ", "##  ", "### ", "####"])

    def test_steps_recursive(self):
        self.assertListEqual(steps_recursive(4), ["#   ", "##  ", "### ", "####"])