class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append new node base on given data argument to the link-list
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = node
        

    def pop(self):
        """
        Delete and return last node value in the link list.
        If link list was empty raise IndexError.
        """
        if self.head is None:
            raise IndexError("Link list is empty")
        elif self.head.next is None:
            # If there is only single node in link list, we should set head equal to None
            data = self.head.data
            self.head = None
        else:
            temp = self.head
            rear = None
            while temp.next is not None:
                rear = temp
                temp = temp.next
            data = temp.data
            rear.next = None
        return data

    def clear(self):
        """
            Clear link list from nodes.
        """
        self.head = None
        return None

    def popitem(self, data):
        """
        Delete first node with same data in link list.
        - Raise IndexError if link-list where empty.
        - Raise ValueError if node with given data not found.
        """
        if self.head is None:
            raise IndexError("Link list is empty")
        elif self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            rear = None
            while temp.next is not None:
                if temp.data == data:
                    break
                rear = temp
                temp = temp.next
            else:
                raise ValueError(
                    "Node with given data was not found in link-list")
            rear.next = temp.next
        return True

    def append_after(self, data, append_after):
        """
        This method will create a new node with given 'data' argument and append it after the node with 
        same value as 'append_after' has.
        - Raise IndexError if link-list was empty.
        - Raise ValueError If There isn't node with same value.
        """
        if self.head is None:
            raise IndexError("Link list is empty")
        temp = self.head
        while temp is not None:
            if temp.data == append_after:
                break
            temp = temp.next
        else:
            raise ValueError(
                f"Node with given value: {append_after} not exists in link-list")
        node = Node(data, temp.next)
        temp.next = node
        return True

    def __contains__(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def __str__(self):
        output = ""
        temp = self.head
        while temp is not None:
            output += f"{temp.data} -> "
            temp = temp.next
        output += "None"
        return output

    def __len__(self):
        i = 0
        temp = self.head
        while temp is not None:
            i += 1
            temp = temp.next
        return i

    def __iter__(self):
        self._node = self.head
        return self

    def __next__(self):
        node = self._node
        if node:
            self._node = node.next
            return node.data
        raise StopIteration
