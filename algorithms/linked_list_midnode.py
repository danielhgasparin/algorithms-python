"""Linked List middle node module.

Find the node at the middle of a Linked List, without using the "size" ot "get_at" methods.
If there are an even number of elements, find the last node of the first half.
"""

def midnode(linked_list):
    """Return the node at the middle of the specified Linked List."""
    if linked_list.get_head() is None:
        return None
    
    current_node = linked_list.get_head()
    ahead_node = linked_list.get_head()

    while ahead_node.next is not None and ahead_node.next.next is not None:
        current_node = current_node.next
        ahead_node = ahead_node.next.next
    
    return current_node