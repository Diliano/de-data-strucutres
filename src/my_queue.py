class Queue():
    def __init__(self, max_size=None):
        self.max_size = max_size
        self._front = 0
        self._back = 0
        self._storage = {}

    def enqueue(self, item):
        if self.max_size is not None and len(self._storage) == self.max_size:
            return "Queue is full"
        self._storage[self._back] = item
        self._back += 1