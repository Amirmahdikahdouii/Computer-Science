import sys
sys.path.append("../")

from unittest import TestCase
from stack import Stack

class StackModuleTest(TestCase):
    @classmethod
    def setUpClass(cls):
        stack = Stack()
        empty_stack = Stack()
        stack.push(3)
        stack.push(2)
        stack.push(1)
        cls.stack = stack
        cls.empty_stack = empty_stack
    
    def test_empty_stack(self):
        # Test stack methods with empty stack
        with self.assertRaises(IndexError):
            self.empty_stack.pop()
        self.assertIsNone(self.empty_stack.peek())
        self.assertEqual(len(self.empty_stack), 0)
        self.assertEqual(self.empty_stack.__str__(), "None")
        
        # Add new node to stack and test the methods
        self.empty_stack.push(1)
        self.assertEqual(len(self.empty_stack), 1)
        self.assertEqual(self.empty_stack.__str__(), "1 -> None")
        self.assertIsNotNone(self.empty_stack.peek())
        self.assertEqual(self.empty_stack.peek(), 1)
        
        # Delete Node from stack and test empty stack again
        self.empty_stack.clean()
        self.assertEqual(len(self.empty_stack), 0)
        self.assertEqual(self.empty_stack.__str__(), "None")
        with self.assertRaises(IndexError):
            self.empty_stack.pop()
        self.assertIsNone(self.empty_stack.peek())
            
    def test_stack(self):
        self.assertEqual(len(self.stack), 3)
        self.assertEqual(self.stack.peek(), 1)
        self.assertIn("1 -> 2 -> 3", self.stack.__str__())
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(len(self.stack), 2)
        
        # Empty the stack
        self.stack.clean()
        self.assertEqual(len(self.stack), 0)