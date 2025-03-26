class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    new_list = s.split(' -> ')
    for i, el in enumerate(new_list):
        res = Node(el, new_list[i])
    return res

print(linked_list_from_string("1 -> 2 -> 3 -> None"))
# Node(1, Node(2, Node(3)))