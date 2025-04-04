class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    odd_head = head
    curr_odd = odd_head
    even_head = head.next
    curr_even = even_head

    while curr_even and curr_odd and curr_even.next and curr_odd.next:
        curr_odd.next = curr_even.next
        curr_odd = curr_odd.next

        curr_even.next = curr_odd.next
        curr_even = curr_even.next

    curr_odd.next = None
    curr_even.next = None

    return Context(odd_head, even_head)