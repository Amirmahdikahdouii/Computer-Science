import sys
sys.path.append("../")

from random import randint
from solution import Employee, LinkList
from unittest import TestCase



class SolutionTest(TestCase):
    def setUp(self):
        self.random_id = [1000, 1001, 1002, 1003]
        self.random_experience = [28, 30, 31, 32]
        self.random_names = ['Jack', "Nina", "John", "Michale"]
        self.list = LinkList()
        for i in range(4):
            self.list.append(
                Employee(self.random_names[i], self.random_id[i], self.random_experience[i]))

    def test_append_employee(self):
        # Append On Existing List
        employee_id = randint(1005, 9999)
        self.list.append(Employee("Billie", employee_id, 10))
        self.assertTrue(employee_id in self.list)

        # Create a new list and append
        l = LinkList()
        l.append(Employee("John", 1000, 31))
        self.assertEqual(l.__str__(), "1000 -> None")
        self.assertTrue(1000 in l)
        self.assertEqual(len(l), 1)
        del l

    def test_pop_employee(self):
        self.assertTrue(1000 in self.list)
        self.assertEqual(4, len(self.list))
        self.list.pop(1000)
        self.assertFalse(1000 in self.list)
        self.assertEqual(3, len(self.list))
        with self.assertRaises(ValueError):
            self.list.pop(1458)
        
    def test_list_display(self):
        expected_output = "1000 -> 1001 -> 1002 -> 1003 -> None"
        self.assertEqual(expected_output, self.list.__str__())
        
        # Create a new list
        l = LinkList()
        l.append(Employee("Amir", 1234, 20))
        self.assertEqual("1234 -> None", l.__str__())
        del l
        
    def test_employee_contains(self):
        self.assertTrue(1000 in self.list)
        self.assertTrue(1003 in self.list)
        self.assertFalse(1546 in self.list)
        self.assertFalse(7542 in self.list)
    
    def test_list_reverse(self):
        # Check reverse single Employee in list
        l = LinkList()
        l.append(Employee("Mike", 4587, 10))
        before_reverse = l.__str__()
        l.reverse()
        after_reverse = l.__str__()
        self.assertEqual(before_reverse, after_reverse)
        
        # Reverse filled list
        before_reverse = self.list.__str__()
        self.list.reverse()
        after_reverse = self.list.__str__()
        self.assertNotEqual(before_reverse, after_reverse)
        self.assertEqual(after_reverse, "1003 -> 1002 -> 1001 -> 1000 -> None")
        
    def test_say_goodby(self):
        """
        Test Say GoodBye
        
        In self.list there are 2 employee with more than 30 years experience, 
        employee ID's are: 1002, 1003
        
        We Expect that say_goodbye method will remove this 2 Id from list.        
        """
        self.assertTrue(1002 in self.list)
        self.assertTrue(1003 in self.list)
        self.assertEqual(4, len(self.list))
        self.list.say_goodby()
        self.assertFalse(1002 in self.list)
        self.assertFalse(1003 in self.list)
        self.assertEqual(2, len(self.list))
        
        # New List With single employee with more than 30 years experience
        l = LinkList()
        l.append(Employee("Jack", 4587, 32))
        self.assertTrue(4587 in l)
        self.assertEqual(1, len(l))
        l.say_goodby()
        self.assertFalse(4587 in l)
        self.assertEqual(0, len(l))

    def test_get_employee(self):
        self.assertEqual(4, len(self.list))
        self.assertIn(1000, [employee.id for employee in self.list])
        
        employee = Employee("Jack", 1000, 28)
        gotted_employee = self.list.get_employee(1000)
        self.assertEqual(employee.id, gotted_employee.id)
        self.assertEqual(employee.full_name, gotted_employee.full_name)
        self.assertEqual(employee.experience, gotted_employee.experience)
        
        self.assertEqual(4, len(self.list))
        self.assertIn(1000, [employee.id for employee in self.list])

        # Get Not Existed Employee
        self.assertIsNone(self.list.get_employee(7895))
        
    def test_list_length(self):
        self.assertEqual(4, len(self.list))
        self.list.pop(1000)
        self.assertEqual(3, len(self.list))
    
    def test_list_iteration(self):
        self.assertEqual(self.random_names, [employee.full_name for employee in self.list])
        self.assertEqual(self.random_id, [employee.id for employee in self.list])
        