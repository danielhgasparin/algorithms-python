import unittest
from algorithms.sort import *

class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertListEqual(bubble_sort([4, 6, 3, 2, 1, 5]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(bubble_sort([12, -1, 3, 44, 90, -20, 5]), [-20, -1, 3, 5, 12, 44, 90])


    def test_selection_sort(self):
        self.assertListEqual(selection_sort([4, 6, 3, 2, 1, 5]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(selection_sort([12, -1, 3, 44, 90, -20, 5]), [-20, -1, 3, 5, 12, 44, 90])


    def test_merge_sort(self):
        self.assertListEqual(merge_sort([4, 6, 3, 2, 1, 5]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(merge_sort([12, -1, 3, 44, 90, -20, 5]), [-20, -1, 3, 5, 12, 44, 90])