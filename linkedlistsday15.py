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
    # Complete this method
    node = Node(data)
    current = head
    current.next = node
    return current
