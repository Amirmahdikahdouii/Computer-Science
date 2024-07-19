class PriorityQueue:
    def __init__(self):
        self._queue = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self._queue[i], self._queue[j] = self._queue[j], self._queue[i]

    def _sift_up(self, index):
        parent = self._parent(index)
        if index > 0 and self._queue[index][0] > self._queue[parent][0]:
            self._swap(index, parent)
            self._sift_up(parent)

    def _sift_down(self, index):
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self._queue) and self._queue[left][0] > self._queue[largest][0]:
            largest = left
        if right < len(self._queue) and self._queue[right][0] > self._queue[largest][0]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._sift_down(largest)

    def push(self, item, priority):
        self._queue.append((priority, item))
        self._sift_up(len(self._queue) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        if len(self._queue) == 1:
            return self._queue.pop()[1]
        item = self._queue[0][1]
        self._queue[0] = self._queue.pop()
        self._sift_down(0)
        return item

    def is_empty(self):
        return len(self._queue) == 0

# Example usage:
pq = PriorityQueue()
pq.push("task1", 1)
pq.push("task2", 4)
pq.push("task3", 3)

while not pq.is_empty():
    print(pq.pop())
