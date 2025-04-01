class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    curr = Node(data)
    curr.next = head
    return curr

def build_one_two_three():
    # Your code goes here.
    return Node(None)