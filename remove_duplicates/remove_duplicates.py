class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head is None or head.next is None:
        return head

    curr = head
    unique = {head.data}
    while curr and curr.next:
        if curr.next.data in unique:
            curr.next = curr.next.next
        else:
            unique.add(curr.next.data)
            curr = curr.next
    
    return head
            
# 1 -> 1 -> 2
