class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError

    first_source = source
    source = source.next
    first_source.next = dest

    return Context(source, first_source)
