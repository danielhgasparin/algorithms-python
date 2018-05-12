"""Tree module."""

from collections import deque

class Node:
    """Node of a tree."""
    def __init__(self, value):
        self.value = value
        self.children = []

    def add(self, value):
        """Add a child with the specified value to this node."""
        self.children.append(Node(value))

    def remove(self, value):
        """Remove any child having the specified value from this node."""
        # Using a slice assignment (children[:] =) the list is modified instead of assign the name to a new list (children =).
        self.children[:] = (child for child in self.children if child.value != value)


class Tree:
    """Tree data structure."""
    def __init__(self):
        self.root = None

    def traverse_breadth_first(self, fn):
        """Traverse the tree breadth first, executing the specified function on each node."""
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            fn(node)
            queue.extend(node.children)

    def traverse_depth_first(self, fn):
        """Traverse the tree depth first, executing the specified function on each node."""
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            fn(node)
            queue.extendleft(reversed(node.children))