"""Binary search tree module.

Binary search tree is a binary tree where all the values to the left of a node are smaller 
than the value of that node, and all values to the right are greater.
"""

class Node:
    """Node of a binary search tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Insert a new value to the binary search tree."""
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        """Return the node containing the specified value."""
        if value == self.value:
            return self

        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return None
            else:
                return self.right.contains(value)