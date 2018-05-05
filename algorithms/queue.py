"""Queue module."""

from collections import deque

class Queue:
    """First element in is the first element out."""
    def __init__(self):
        self._queue = deque()

    def enqueue(self, element):
        """Add element to end of the queue."""
        self._queue.append(element)

    def dequeue(self):
        """Remove element at the start of the queue."""
        return self._queue.popleft()

    def peek(self):
        """Get the element at the start of the queue without removing it."""
        return self._queue[0]