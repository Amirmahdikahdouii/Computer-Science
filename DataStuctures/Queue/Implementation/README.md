# Queue

## Python Implementation:

In this directory there is a **queue.py** file that has implementation of **Queue** Data Structure using python language and also not using python list or other built-in python data structure. It's all pure and you will be find out by reading the source.

Also Methods has some docstring that **I suggest you to read them for better understanding**. You can define your queue and test methods and functionalities.

Here is a basic example:

```python
# Initialize Instance 
queue = Queue()

# Add some names to queue
queue.enqueue("Jack")
queue.enqueue("Michel")
queue.enqueue("Ana")

# work with queue
print(queue) # Jack <- Michel <- Ana <- None
print(len(queue)) # 3
print("Jack" in queue) # True
for person in queue:
    print(person)
# Output:
# jack
# Michel
# Ana    

# Delete from queue
queue.dequeue()

print(queue) # Michel <- Ana <- None
print(len(queue)) # 2
print("Jack" in queue) # False
```

### TestCases for module:

There is a **Test/** directory in this path that have a **test_queue.py** file. For Testing module you can use this file to check the implementation and also have your own TestCases.

- [ ] Write Tesk Case for module