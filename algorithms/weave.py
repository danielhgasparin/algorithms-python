"""Weave module."""

from algorithms.queue import Queue

def weave(queue_a, queue_b):
    """Return a queue containing the values of the two received queues, alternating between the values of each one."""
    result = Queue()
    while queue_a.peek() is not None or queue_b.peek() is not None:
        if queue_a.peek() is not None:
            result.enqueue(queue_a.dequeue())
        if queue_b.peek() is not None:
            result.enqueue(queue_b.dequeue())
    return result