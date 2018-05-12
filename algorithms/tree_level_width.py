"""Tree level width module."""

from collections import deque

def tree_level_width(tree):
    """Return a list containing the width of each level of the specified tree."""
    result = []
    count = 0
    queue = deque([tree.root, "s"])
    while len(queue) > 0:
        node = queue.popleft()
        if node == "s":
            if(count == 0):
                break
            else:
                result.append(count)
                count = 0
                queue.append("s")
        else:
            count += 1
            queue.extend(node.children)
    return result