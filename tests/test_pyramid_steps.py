import unittest
from algorithms.pyramid_steps import *

class TestPyramidSteps(unittest.TestCase):
    def test_pyramid_steps_just(self):
        self.assertListEqual(pyramid_steps_concat(1), ["#"])
        self.assertListEqual(pyramid_steps_concat(2), [" # ", "###"])
        self.assertListEqual(pyramid_steps_concat(3), ["  #  ", " ### ", "#####"])


    def test_pyramid_steps_loop(self):
        self.assertListEqual(pyramid_steps_loop(1), ["#"])
        self.assertListEqual(pyramid_steps_loop(2), [" # ", "###"])
        self.assertListEqual(pyramid_steps_loop(3), ["  #  ", " ### ", "#####"])


    def test_pyramid_steps_recursive(self):
        self.assertListEqual(pyramid_steps_recursive(1), ["#"])
        self.assertListEqual(pyramid_steps_recursive(2), [" # ", "###"])
        self.assertListEqual(pyramid_steps_recursive(3), ["  #  ", " ### ", "#####"])