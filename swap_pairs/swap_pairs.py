class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head

    start_next = head.next
    head.next = swap_pairs(start_next.next)
    start_next.next = head

    return start_next
