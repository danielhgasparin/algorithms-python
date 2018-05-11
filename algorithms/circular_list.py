"""Circular list module."""

def is_circular(linked_list):
    """Check if the specified Linked List is circular."""
    if linked_list.get_head() is None:
        return False
    
    current_node = linked_list.get_head()
    ahead_node = linked_list.get_head()

    while ahead_node.next is not None and ahead_node.next.next is not None:
        current_node = current_node.next
        ahead_node = ahead_node.next.next
        if current_node is ahead_node:
            return True
    
    return False