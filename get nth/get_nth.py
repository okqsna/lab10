def get_nth(node, index):
    curr_el = node
    counter = 0
    while curr_el:
        if counter == index:
            return curr_el
        curr_el = curr_el.next
        counter += 1
    if counter < index or index < 0 or node is None:
        raise IndexError
