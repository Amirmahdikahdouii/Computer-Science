class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        """
        Remove first item from stack
        """
        if self.top is None:
            raise IndexError("Stack is empty")
        node = self.top
        data = node.data
        self.top = node.next
        del node
        return data

    def peek(self):
        """
        Return first stack node data
        """
        if self.top is None:
            return None
        return self.top.data

    def push(self, data):
        """
        Create a new node and fill it with given data, and then push it into stack.
        """
        node = Node(data)
        node.next = self.top
        self.top = node

    def __len__(self):
        """
        Return Length of the stack
        """
        if self.top is None:
            return 0
        temp = self.top
        i = 1
        while temp.next is not None:
            i += 1
            temp = temp.next
        return i
    
    def __str__(self):
        """
        Return str object of stack nodes data.
        If stack is empty return str obj equal to "None".
        Example:
        # If We have a stack that has 3 items below, the output will be:
        1 -> 2 -> 3 -> None
        """
        output = ""
        temp = self.top
        while temp is not None:
            output += f"{temp.data} -> "
            temp = temp.next
        output += "None"
        return output
    
    def clean(self):
        """
        Empty the stack whenever you call it.
        """
        while self.top is not None:
            t = self.top
            self.top = t.next
            del t
        