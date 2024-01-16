class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._node = None

    def is_empty(self):
        """
        Return True If Queue was empty and if not, return False.
        """
        return self.front is None

    def enqueue(self, data):
        """
        Create and append new node with given data to the Queue.
        """
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        return True

    def dequeue(self):
        """
        Delete node from the queue.
        Note: in Queue data structure, we delete node from beginning of queue.
        """
        if not self.is_empty():
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear is None
            return data
        raise IndexError("Queue is empty")

    def __str__(self):
        """
        Display the Queue with nodes data.
        """
        output = ""
        temp = self.front
        while temp is not None:
            output += f"{temp.data} <- "
            temp = temp.next
        output += "None"
        return output

    def __len__(self):
        """
        Return length of queue
        """
        i = 0
        current = self.front
        while current:
            i += 1
            current = current.next
        return i

    def __contains__(self, item):
        """
        This Method check if there is a node with the same "item" parameter in the Queue or not.
        If there is a node, return True otherwise return False.
        """
        current = self.front
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self):
        # I set the _node in this method because it will call before __next__ and we can loop from
        # first node in Queue.
        # Note That this way is not optimize yet and I'm searching for some better implementation.
        self._node = self.front
        return self

    def __next__(self):
        """
        This Method with this structure is only use whenever you loop over the queue.
        ** Note that it is not useful to use queue with next() method! **
        """
        if self._node is not None:
            data = self._node.data
            self._node = self._node.next
            return data
        raise StopIteration
