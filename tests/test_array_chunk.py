import unittest
from algorithms.array_chunk import *

class TestArrayChunk(unittest.TestCase):
    def test_array_chunk_slice(self):
        self.assertListEqual(array_chunk_slice([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertListEqual(array_chunk_slice([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertListEqual(array_chunk_slice([1, 2, 3, 4, 5], 10), [[1, 2, 3, 4, 5]])


    def test_array_chunk_loop(self):
        self.assertListEqual(array_chunk_loop([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertListEqual(array_chunk_loop([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertListEqual(array_chunk_loop([1, 2, 3, 4, 5], 10), [[1, 2, 3, 4, 5]])