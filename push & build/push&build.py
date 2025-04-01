class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    curr = Node(data)
    curr.next = head
    return curr

def build_one_two_three():
    linkedlist = None
    for i in range(3, 0, -1):
        linkedlist = push(linkedlist, i)
    return linkedlist