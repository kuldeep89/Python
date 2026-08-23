"""Utilities for creating singly linked lists."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_ll(values):
    """Create a linked list from an iterable and return its head node."""
    head = None
    tail = None

    for value in values:
        new_node = Node(value)
        if head is None:
            head = new_node
        else:
            tail.next = new_node
        tail = new_node

    return head

def print_ll(head):
    """Print the linked list starting from the head node."""
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
