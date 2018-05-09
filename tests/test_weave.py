import unittest
from algorithms.queue import Queue
from algorithms.weave import *

class TestWeave(unittest.TestCase):
    def test_weave(self):
        queue_a = Queue()
        queue_a.enqueue(1)
        queue_a.enqueue(2)
        queue_a.enqueue(3)
        queue_a.enqueue(4)
        queue_b = Queue()
        queue_b.enqueue("a")
        queue_b.enqueue("b")
        result = weave(queue_a, queue_b)
        self.assertEqual(result.dequeue(), 1)
        self.assertEqual(result.dequeue(), "a")
        self.assertEqual(result.dequeue(), 2)
        self.assertEqual(result.dequeue(), "b")
        self.assertEqual(result.dequeue(), 3)
        self.assertEqual(result.dequeue(), 4)
        with self.assertRaises(IndexError):
            result.dequeue()

        queue_a = Queue()
        queue_a.enqueue(1)
        queue_a.enqueue(2)
        queue_b = Queue()
        queue_b.enqueue("a")
        queue_b.enqueue("b")
        queue_b.enqueue("c")
        queue_b.enqueue("d")
        result = weave(queue_a, queue_b)
        self.assertEqual(result.dequeue(), 1)
        self.assertEqual(result.dequeue(), "a")
        self.assertEqual(result.dequeue(), 2)
        self.assertEqual(result.dequeue(), "b")
        self.assertEqual(result.dequeue(), "c")
        self.assertEqual(result.dequeue(), "d")
        with self.assertRaises(IndexError):
            result.dequeue()