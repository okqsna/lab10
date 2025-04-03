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
    unique = []
    while curr and curr.next:
        if curr.next.data not in unique:
            unique.append(curr.next.data)
            curr = curr.next
        else:
            curr.next = curr.next.next
    
    return head
            

# 1 -> 1 -> 2
