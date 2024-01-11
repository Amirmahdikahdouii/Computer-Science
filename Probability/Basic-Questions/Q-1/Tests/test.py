import sys
sys.path.append("../")

from unittest import TestCase
from solution import calculate_answers
from itertools_solving import calculate_answers as itertools_calculate_answers

class TestSolutionModule(TestCase):
    """
    TestCases for writed modules to calculate probability of sum 7 when rolling 2 dice
    """
    
    def setUp(self):
        self.answer = calculate_answers()
        self.itertools_answer = itertools_calculate_answers()
        self.expected_answer = [(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)]
        return super().setUp()
    
    def test_calculate_answers(self):
        self.assertEqual(self.answer[0], 6/36)
        self.assertNotEqual(self.answer[0], 5/36)
        self.assertNotEqual(self.answer[0], 7/36)
        self.assertIn((1, 6), self.answer[1])
        self.assertNotIn((2, 3), self.answer[1])
        self.assertCountEqual(self.answer[1], self.expected_answer)
        self.assertEqual(self.answer[1], self.expected_answer)
    
    def test_itertools_calculate_answers(self):
        self.assertEqual(self.itertools_answer[0], 6/36)
        self.assertNotEqual(self.itertools_answer[0], 5/36)
        self.assertNotEqual(self.itertools_answer[0], 7/36)
        self.assertIn((1, 6), self.itertools_answer[1])
        self.assertNotIn((2, 3), self.itertools_answer[1])
        self.assertCountEqual(self.itertools_answer[1], self.expected_answer)
        self.assertEqual(self.itertools_answer[1], self.expected_answer)