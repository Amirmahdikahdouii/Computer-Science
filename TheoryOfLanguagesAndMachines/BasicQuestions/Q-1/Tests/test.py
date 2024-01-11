import sys
sys.path.append("../")

from unittest import TestCase
from solution import cartesian_product

class TestCartesianProduct(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = list(cartesian_product([0, 1], repeat=2))
        cls.expected_result = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    def test_valid_data(self):
        self.assertEqual(self.result, self.expected_result)
        self.assertEqual(list(cartesian_product([0, 1], repeat=3)), [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)])
        self.assertEqual(list(cartesian_product(["a", "b"], repeat=2)), [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')])
        self.assertNotEqual(list(cartesian_product(["a", "b"], repeat=3)), [('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b')])
        self.assertEqual(len(list(cartesian_product([0, 1], repeat=4))), 16)
        
    def test_invalid_data(self):
        with self.assertRaises(TypeError):
            list(cartesian_product(2))
        with self.assertRaises(TypeError):
            list(cartesian_product((2, 1), 2))