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
        nodes = deque([self.root])
        while len(nodes) > 0:
            node = nodes.popleft()
            fn(node)
            nodes.extend(node.children)

    def traverse_depth_first(self, fn):
        nodes = deque([self.root])
        while len(nodes) > 0:
            node = nodes.popleft()
            fn(node)
            nodes.extendleft(reversed(node.children))