class Stack:
    '''Stack implementation'''

    def __init__(self, items=None, max_size=None):
        self.items = items if items is not None else []
        self.max_size = max_size

    def push(self, item):
        if self.max_size is None or len(self.items) < self.max_size:
            self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return self.max_size is not None and len(self.items) == self.max_size

    def search(self, item):
        for index, value in enumerate(reversed(self.items)):
            if value == item:
                return index
        return -1

