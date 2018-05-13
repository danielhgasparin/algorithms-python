"""Stack module."""

class Stack:
    """First element in is the last element out."""
    def __init__(self):
        self._stack = []


    def push(self, element):
        """Add element to the top of the stack."""
        self._stack.append(element)


    def pop(self):
        """Remove element at the top of the stack."""
        return self._stack.pop()


    def peek(self):
        """Get the element at the top of the stack without removing it."""
        try:
            return self._stack[-1]
        except IndexError:
            return None