# Balanced Parentheses:

**Question:** Write a Python program to check if a given string of parentheses is balanced or not. 

For example, **(()()()())** and **(((())))** are balanced, but **(()(** and **(()))** are not.

## How to Solve:
```python
def check_string(string: str):
    """
    Description of How This Method Work:
    This Method will get a string and check that given string has valid and balanced parentheses or not.
    The Idea is that we will append open parentheses into stack and pop them if character was close
    parentheses. 
    At the end if there is remain Item in stack, It means that parentheses are not Balanced.
    Also if there was no open parentheses in stack and we got ')', It mean that parentheses are not Balanced.
    """
    ...
```

### Tests:
There is a file named: **solution.py** in this directory that has implementation of **Stack** data structure and also a method **check_string** that will get a string and check that string's parentheses are balanced or not.

