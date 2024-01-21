import sys

sys.path.append("../")

from unittest import TestCase
from linklist import LinkList

class LinkListTest(TestCase):
    def setUp(self):
        self.list = LinkList()
        self.list.append("LG")
        self.list.append("Samsung")
        self.list.append("Apple")
    
    def test_append(self):
        # Create a new list
        l = LinkList()
        self.assertFalse("BMW" in l)
        l.append("BMW")
        self.assertTrue("BMW" in l)
        self.assertEqual(len(l), 1)
        del l
        
        # Append to the existing list
        self.assertEqual(len(self.list), 3)
        self.assertFalse("Asus" in self.list)
        self.list.append("Asus")
        self.assertTrue("Asus" in self.list)
        
    def test_pop(self):
        # Create and test on new list
        l = LinkList()
        
        # Test pop data from empty list
        with self.assertRaises(IndexError):
            l.pop()
        
        l.append("Benz")
        l.append("BMW")
        l.append("Ferrari")
        self.assertEqual(3, len(l))
        data = l.pop()
        self.assertEqual("Ferrari", data)
        self.assertFalse("Ferrari" in l)
        self.assertEqual(2, len(l))
        del l, data
        
        # Test on Existing List
        self.assertTrue("Apple" in self.list)
        data = self.list.pop()
        self.assertFalse("Apple" in self.list)
        self.assertEqual(data, "Apple")
        del data
        
    def test_popitem(self):
        self.assertTrue("LG" in self.list)
        self.list.popitem("LG")
        self.assertFalse("LG" in self.list)
                         
        # Test not exist data:
        with self.assertRaises(ValueError):
            self.list.popitem("Microsoft")
        
        # Try to append on a empty list
        with self.assertRaises(IndexError):
            self.list.clear()
            self.list.popitem("LG")
        
    def test_clear(self):
        self.assertEqual(3, len(self.list))
        self.list.clear()
        self.assertEqual(0, len(self.list))
        
    def test_append_after(self):
        self.assertEqual("LG -> Samsung -> Apple -> None", str(self.list))
        self.assertEqual(len(self.list), 3)
        self.assertFalse("Sony" in self.list)
        self.list.append_after("Sony", "LG")
        self.assertEqual("LG -> Sony -> Samsung -> Apple -> None", str(self.list))
        self.assertEqual(len(self.list), 4)
        self.assertTrue("Sony" in self.list)
        
        # Try on data that does'nt exists:
        with self.assertRaises(ValueError):
            self.list.append_after("Google", "Asus")
        
        # Try to append on a empty list
        with self.assertRaises(IndexError):
            self.list.clear()
            self.list.append_after("Google", "LG")
        
    def test_contains(self):
        self.assertTrue("LG" in self.list)
        self.assertTrue("Samsung" in self.list)
        self.assertFalse("Asus" in self.list)
        self.assertFalse("Sony" in self.list)
        
    def test_str(self):
        self.assertEqual("LG -> Samsung -> Apple -> None", str(self.list))
        self.list.pop()
        self.assertEqual("LG -> Samsung -> None", str(self.list))
        self.list.clear()
        self.assertEqual("None", str(self.list))
        
    def test_len(self):
        self.assertEqual(3, len(self.list))
        self.list.append("Sony")
        self.assertEqual(4, len(self.list))
        self.list.popitem("LG")
        self.assertEqual(3, len(self.list))
        self.list.clear()
        self.assertEqual(0, len(self.list))
        
    def test_iterable(self):
        """
        Test looping on list to get the data and find out work correct or not.
        list comprehension in python: https://realpython.com/list-comprehension-python/
        """
        self.assertEqual(['LG', 'Samsung', 'Apple'], [data for data in self.list])
        self.assertTrue(['LG', 'Samsung', 'Apple'], [data for data in self.list])