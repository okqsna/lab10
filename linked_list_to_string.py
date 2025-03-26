class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    nodes = ''
    while node:
        nodes += str(node.data) + ' -> '
        if node.next == None:
            nodes += 'None'
        node = node.next
    return nodes

print(stringify(Node(0, Node(1, Node(2, Node(3))))))