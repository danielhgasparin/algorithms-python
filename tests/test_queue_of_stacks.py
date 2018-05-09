import unittest
from algorithms.queue_of_stacks import *

class TestQueueOfStacks(unittest.TestCase):
    def test_queue_of_stacks(self):
        queue = QueueOfStacks()
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