from stack import Stack

class PalindromStack(Stack):
    def __str__(self):
        temp = self.top
        string = ""
        while temp:
            string += f"{temp.data}"
            temp = temp.next
        return string

def is_palindromic(string: str):
    """
    Check that is given string palindromic or no using Stack Data Structure
    
    >>> palindromic("Wow")
    True
    
    >>> palindromic("now")
    False
    
    Args:
        string: str -> String that wanna check
    
    Return:
    Boolen -> Represent that given string was palindromic or not
    """
    string = string.lower()
    stack = PalindromStack()
    for char in string:
        stack.push(char)
    return string == str(stack)
    