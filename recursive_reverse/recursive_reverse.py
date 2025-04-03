class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head

    curr = reverse(head)
    curr.next.next = head
    curr.next = None
    
    return curr