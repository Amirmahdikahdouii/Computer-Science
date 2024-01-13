# Stack Implementation

## Python Implementation

There is a python file named: **stack.py** that has Node and Stack Object implementation and you can define your stack by get an instance from Stack object, and then push values, pop and empty stack, print it and get length of stack by methods. 

**There are docstring in every method that can help you!**

There is also a test module in **Tests/** directory that you can run it and test the stack work correctly or no.

#### Example:

```python
stack = Stack()
stack.push(3)
stack.push(2)
stack.push(1)
print(stack)
print(len(stack))
print(stack.peek())
print(stack.pop())
stack.clean()
print(stack)
print(len(stack))
```