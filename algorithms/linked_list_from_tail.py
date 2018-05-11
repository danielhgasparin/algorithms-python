"""Linked list from tail module.

Find the node at the specified index, starting with index 0 from the tail, without using the "size" ot "get_at" methods.
"""

def get_from_tail(linked_list, index):
    """Return the node at the specified index starting from the tail."""
    if linked_list.get_head() is None:
        return None

    ahead_node = linked_list.get_head()
    for _ in range(index):
        if ahead_node.next is None:
            return None
        ahead_node = ahead_node.next

    current_node = linked_list.get_head()
    while ahead_node.next is not None:
        ahead_node = ahead_node.next
        current_node = current_node.next

    return current_node