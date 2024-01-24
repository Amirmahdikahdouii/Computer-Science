import sys
sys.path.append("../")

from unittest import TestCase
from solution import is_palindromic, PalindromStack

class PalindromicStackTest(TestCase):
    @staticmethod
    def fill_stack(string: str):
        stack = PalindromStack()
        for char in string:
            stack.push(char)
        return stack
        
    def test_str(self):
        """
        Test Stack.__str__()
        """
        stack = self.fill_stack("Tokyo")
        self.assertEqual("Tokyo"[::-1], str(stack))
        stack = self.fill_stack("Tehran")
        self.assertEqual("Tehran"[::-1], str(stack))
        stack = self.fill_stack("Los Angeles")
        self.assertEqual("Los Angeles"[::-1], str(stack))
        
class SolutionTest(TestCase):
    def test_palindromic(self):
        """
        Test is_palindromic returned value
        """
        self.assertTrue(is_palindromic("Wow"))
        self.assertTrue(is_palindromic("HEH"))
        self.assertTrue(is_palindromic("leVel"))
        self.assertTrue(is_palindromic("abCcBA"))
        
        self.assertFalse(is_palindromic("Python"))
        self.assertFalse(is_palindromic("Django"))
        self.assertFalse(is_palindromic("Flask"))
        self.assertFalse(is_palindromic("fastapi"))