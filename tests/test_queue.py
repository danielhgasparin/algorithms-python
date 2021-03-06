import unittest
from algorithms.queue import Queue

class TestQueue(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.peek(), None)
        with self.assertRaises(IndexError):
            queue.dequeue()