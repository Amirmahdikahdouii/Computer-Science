import sys

sys.path.append("../")

from unittest import TestCase
from solution import check_string, Stack

class StackTest(TestCase):
    """
        Test Cases for Stack and methods
    """
    
    def setUp(self):
        self.stack = Stack()
        self.stack.append("Iran")
        self.stack.append("Iraq")
        self.stack.append("India")
    
    def test_append(self):
        stack = Stack()
        self.assertEqual(0, len(stack))
        stack.append("Madrid")
        self.assertEqual(1, len(stack))
        self.assertTrue("Madrid" in stack)
        stack.append("Milan")
        self.assertEqual(2, len(stack))
        self.assertTrue("Milan" in stack)
        del stack
        
    def test_pop(self):
        self.assertTrue("India" in self.stack)
        self.stack.pop()
        self.assertFalse("India" in self.stack)
        self.assertTrue("Iraq" in self.stack)
        self.stack.pop()
        self.assertFalse("Iraq" in self.stack)
        self.assertEqual(1, len(self.stack))
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.pop()
            
    def test_peek(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()
        stack.append("USA")
        self.assertEqual(stack.peek(), "USA")
        stack.append("Germany")
        self.assertEqual(stack.peek(), "Germany")
        del stack
        
        
    def test_contains(self):
        self.assertTrue("India" in self.stack)
        self.assertTrue("Iran" in self.stack)
        self.assertTrue("Iraq" in self.stack)
        
        self.assertFalse("China" in self.stack)
        self.assertFalse("UAE" in self.stack)
        self.assertFalse("South Korea" in self.stack)
        
    def test_stack_length(self):
        self.assertEqual(3, len(self.stack))
        self.stack.pop()
        self.assertEqual(2, len(self.stack))
        self.stack.append("UAE")
        self.assertEqual(3, len(self.stack))
        
        # Test Empty Stack
        stack = Stack()
        self.assertEqual(0, len(stack))
        self.assertTrue(0 == len(stack))
        del stack
        
        
    def test_stack_loop(self):
        """
        Test Loop over the stack, by list comprehension
        """
        self.assertEqual(["India", "Iraq", "Iran"], [country for country in self.stack])
        self.stack.pop()
        self.assertEqual(["Iraq", "Iran"], [country for country in self.stack])
        self.stack.pop()
        self.assertTrue("Iran" in [country for country in self.stack])
        
    
class CheckStringTest(TestCase):
    """
        Test Cases for check_string method
    """
    def test_strings(self):
        self.assertTrue(check_string("((()))"))
        self.assertTrue(check_string("()()()"))
        self.assertTrue(check_string("(1 + 2) * 5"))
        self.assertFalse(check_string("(10 + 6"))
        self.assertFalse(check_string("((()"))
        self.assertFalse(check_string("("))
        self.assertFalse(check_string(")"))