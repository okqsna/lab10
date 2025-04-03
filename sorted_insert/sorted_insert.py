class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list
    if head is None:
        return Node(data)
    node_to_be_inserted = Node(data)
    curr_node = head

    if data < head.data:
        node_to_be_inserted.next = curr_node
        return node_to_be_inserted

    while curr_node.next and curr_node.next.data < data:
        curr_node = curr_node.next

    curr_node.next = node_to_be_inserted
    node_to_be_inserted.next = curr_node.next

    return head
