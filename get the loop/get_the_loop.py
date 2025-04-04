def loop_size(node):
    loop = False
    first = node.next
    second = node.next.next
    counter = 0

    while first and first.next and second and second.next:
        if first == second:
            loop = True
            break
        first = first.next
        second = second.next.next

    if loop:
        first = first.next
        counter += 1
        while first != second:
            first = first.next
            counter += 1
    return counter
