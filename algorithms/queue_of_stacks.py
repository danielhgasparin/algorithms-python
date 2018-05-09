"""Queue of stacks module."""

from algorithms.stack import Stack

class QueueOfStacks:
    """A queue implemented using two stacks."""
    def __init__(self):
        self._stack_in = Stack()
        self._stack_out = Stack()

    def enqueue(self, element):
        """Add element to the end of the queue."""
        self._move_in()
        self._stack_in.push(element)

    def dequeue(self):
        """Remove element at the start of the queue."""
        self._move_out()
        return self._stack_out.pop()

    def peek(self):
        """Get the element at the start of the queue without removing it."""
        self._move_out()
        return self._stack_out.peek()

    def _move_in(self):
        while self._stack_out.peek() is not None:
            self._stack_in.push(self._stack_out.pop())

    def _move_out(self):
        while self._stack_in.peek() is not None:
            self._stack_out.push(self._stack_in.pop())