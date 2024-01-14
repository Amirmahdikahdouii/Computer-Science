import sys
sys.path.append("../")

from unittest import TestCase
from solution import DFA

class DFATest(TestCase):
    @classmethod
    def setUpClass(cls):
        quantities = ["A", "B", "C", "D"]
        alphabet = ['a', 'b']
        start_state = "A"
        final_states = ["B"]
        cls.dfa = DFA(quantities, alphabet, start_state, final_states)
    
    def test_ok_strings(self):
        self.dfa.string = "abababa"
        self.assertTrue(self.dfa.check())
        self.assertEqual(self.dfa.__str__(), "True")
        
        self.dfa.string = "aba"
        self.assertTrue(self.dfa.check())
        self.assertEqual(self.dfa.__str__(), "True")
        
        self.dfa.string = "aaaabbb"
        self.assertTrue(self.dfa.check())
        self.assertEqual(self.dfa.__str__(), "True")
        
    def test_fail_strings(self):
        """
        In this test we have failed strings that should not accept by machine
        """
        self.dfa.string = "abababab"
        self.assertFalse(self.dfa.check())
        self.assertEqual(self.dfa.__str__(), "False")
        
        self.dfa.string = ""
        self.assertFalse(self.dfa.check())
        self.assertEqual(self.dfa.__str__(), "False")
        
        self.dfa.string = "bab"
        self.assertFalse(self.dfa.check())
        self.assertEqual(self.dfa.__str__(), "False")
        
    def test_raise_exception(self):
        """
        In this test we try to achive raises by machine with failed string that character is not in alphabet and 
        wrong state that is not defined.
        """
        self.dfa.string = "abc"
        
        with self.assertRaises(ValueError):
            self.dfa.check()
        with self.assertRaisesRegex(ValueError, "character is not in alphabet"):
            self.dfa.check()
            
        # Test State not in quantities
        self.dfa.start_position = "G"
        self.dfa.string = "aba"
        with self.assertRaises(ValueError):
            self.dfa.check()
        with self.assertRaisesRegex(ValueError, "given state is not in quantities"):
            self.dfa.check()