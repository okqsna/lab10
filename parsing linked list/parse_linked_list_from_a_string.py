class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data} -> {self.next}'

def linked_list_from_string(s):
    new_list = s.split(' -> ')
    if len(new_list) == 0 or new_list[0] == 'None':
        return None
    head = Node(int(new_list[0]))
    curr = head

    for el in new_list[1:]:
        if el != 'None':
            curr.next = Node(int(el))
            curr = curr.next
    return head

print(linked_list_from_string("1 -> 2 -> 3 -> None"))
# Node(1, Node(2, Node(3)))