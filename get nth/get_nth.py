"""
Getting nth from LinkedList
"""

def get_nth(node, index):
    if index < 0 or node is None:
        raise IndexError

    curr_el = node
    counter = 0

    while curr_el:
        if counter == index:
            return curr_el
        if curr_el is not None:
            counter += 1
        curr_el = curr_el.next

    if counter < index:
        raise IndexError
