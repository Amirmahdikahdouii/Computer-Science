class Node:
    def __init__(self, data: str, next=None):
        self.data = data
        self.next = next

class Stack:
    """
    Stack DataStructure Implementation to solve the Problem
    """
    
    def __init__(self):
        self.top: Node = None
        
    def append(self, char: str):
        """
        Append Character of string in a stack
        """
        node = Node(char)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    
    def pop(self):
        """
        Delete and return top node from stack.
        - If stack was empty, it will raise IndexError.
        """
        if self.top is None:
            raise IndexError("Stack is Empty")
        node = self.top
        self.top = node.next
        return node.data
    
    def peek(self):
        """
        Return top item data's from Stack.
        - If Stack was empty, It will raise IndexError
        Note: This Method doesn't remove node from Stack!
        """
        if self.top is None:
            raise IndexError("Stack is Empty")
        return self.top.data
    
    def __str__(self):
        """
            Return string of Stack schema
        """
        temp = self.top
        output = ""
        while temp:
            output += f"| {temp.data} |\n"
            temp = temp.next
        return output

    def __len__(self):
        i = 0
        temp = self.top
        while temp:
            temp = temp.next
            i += 1
        return i
    
    def __contains__(self, data):
        temp = self.top
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False
    
    def __iter__(self):
        self.iter_top = self.top
        return self

    def __next__(self):
        if self.iter_top:
            node = self.iter_top
            self.iter_top = node.next
            return node.data
        raise StopIteration
    
def check_string(string: str):
    """
    Check That parentheses in string are balanced or not.
    
    Args:
    string: str -> Given string for checking by method.
    
    >>> check_string("((()))")
    True
    
    >>> check_string("())")
    False
    
    Return Type: Boolean -> Return True if parentheses was balanced in string otherwised return False
    """
    stack = Stack()
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                # Check that if There is no '(' in stack, the parentheses is not balanced
                return False
            stack.pop()
    return len(stack) == 0
