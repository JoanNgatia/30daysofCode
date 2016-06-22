# still not working tho :-(


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print current.data,
            current = current.next


def insert(self, head, data):
    # Complee this method
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next:
            current = current.next
            current.next = new_node
    return head
