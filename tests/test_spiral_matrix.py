import unittest
from algorithms.spiral_matrix import *

class TestSpiralMatrix(unittest.TestCase):
    def test_spiral_matrix(self):
        self.assertListEqual(spiral_matrix(1), [[1]])

        self.assertListEqual(spiral_matrix(2), [[1, 2],
                                                [4, 3]])

        self.assertListEqual(spiral_matrix(3), [[1, 2, 3],
                                                [8, 9, 4],
                                                [7, 6, 5]])

        self.assertListEqual(spiral_matrix(4), [[ 1,  2,  3,  4],
                                                [12, 13, 14,  5],
                                                [11, 16, 15,  6],
                                                [10,  9,  8,  7]])