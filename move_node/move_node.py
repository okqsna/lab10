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
        return None
    first_source = source
    source = source.next
    dest.next = dest
    dest = first_source

    return Context(first_source, dest)
