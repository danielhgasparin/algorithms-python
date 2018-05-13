"""Linked list module."""

class Node:
    """Node of a linked list."""
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    """Linked List data structure."""
    def __init__(self, head = None):
        self.head = head


    def __iter__(self):
        """Make this class iterable implementing the "__next__" method."""
        self.iter_current = self.head
        return self


    def __next__(self):
        """Get next element while iterating. Must raise "StopIteration" after the last element."""
        if self.iter_current is not None:
            node = self.iter_current
            self.iter_current = self.iter_current.next
            return node
        else:
            raise StopIteration


    # def __iter__(self):
    #     """Make this class iterable using a generator."""
    #     current = self.head
    #     while current is not None:
    #         yield current
    #         current = current.next


    def insert(self, value):
        """Insert a new value to the linked list."""
        self.head = Node(value, self.head)


    def size(self):
        """Get the number of elements in the linked list at the head."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


    def get_head(self):
        """Get the head node."""
        return self.head


    def get_tail(self):
        """Get the tail node."""
        if self.head is None:
            return None

        current = self.head
        while current.next is not None:
            current = current.next
        return current


    def clear(self):
        """Empty the linked list."""
        self.head = None


    def remove_head(self):
        """Remove the head node."""
        if self.head is not None:
            self.head = self.head.next
    

    def remove_tail(self):
        """Remove the tail node."""
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        previous = self.head
        current = self.head.next
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None


    def insert_tail(self, value):
        """Insert a new value to the linked list at the tail."""
        node = Node(value)
        tail = self.get_tail()
        if tail is None:
            self.head = node
        else:
            tail.next = node
        

    def get_at(self, index):
        """Get the element at the specified index."""
        count = 0
        current = self.head
        while current is not None:
            if count == index:
                return current
            current = current.next
            count += 1
        return None


    def remove_at(self, index):
        """Remove the element at the specified index."""
        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next

        previous = self.get_at(index - 1)
        if previous is None or previous.next is None:
            return

        previous.next = previous.next.next


    def insert_at(self, index, value):
        """Insert a new value to the linked list at the specified index."""
        if self.head is None or index == 0:
            self.head = Node(value, self.head)
            return

        # Get the node before the specified index or, if it not exists, at the tail.
        previous = self.get_at(index - 1) or self.get_tail()

        previous.next = Node(value, previous.next)