class Employee:
    def __init__(self, full_name: str, id: int, experience: int, next=None):
        self.full_name = full_name
        self.id = id
        self.experience = experience
        self.next = next


class LinkList:
    def __init__(self):
        self.first = None

    def append(self, employee: Employee):
        """
        Append node to the LinkList

        Args:
            employee (Employee): An Employee Object that is also a Link List Node.
        """
        if self.first is None:
            self.first = employee
        else:
            t = self.first
            while t.next is not None:
                t = t.next
            t.next = employee

    def pop(self, employee_id: int):
        """
        Return Employee object from Link List if it's found otherwise raise ValueError.
        Arg:
            employee_id: Integer that represent Employee ID.
        """
        if self.first is None:
            raise IndexError("Link List is Empty")
        node = self.first
        if node.id == employee_id:
            # Check the first node
            self.first = node.next
            return node

        temp = node
        node = node.next
        while node.next is not None:
            if node.id == employee_id:
                temp.next = node.next
                return node
            temp = node
            node = node.next
        raise ValueError("Employee Doesn't exists")

    def __str__(self):
        """
        Return and display link list based on employees Id.
        """
        output = ""
        t = self.first
        while t is not None:
            output += f"{t.id} -> "
            t = t.next
        output += "None"
        return output

    def __contains__(self, employee_id: int):
        """
        Search Employee in Link List based on employee ID.
        If Employee with same ID exists return True, and if not, return False.
        Arg:
            employee_id: Integer that is lookup for employee in Link List
        """
        t = self.first
        while t is not None:
            if t.id == employee_id:
                return True
            t = t.next
        return False

    def reverse(self):
        """
        Reverse The Link List ordering without creating a new list
        Description:
        The Idea is to reverse the node.next pointer of every list node to point
        to the previous node in list.
        We Do this by having 2 Nodes in each count of loop and change their pointer.
        - At the end it is important to set the last element pointer to the previous one
        - And set the self.first pointer (That actually is last node in list after reversing) equal to None
          to avoid the looping the last two nodes pointers.
        - After them, we set self.first to point at first node in list.
        """
        if self.first is None or self.first.next is None:
            # Return self.first if there is less or equal than 1 node in list
            return self.first
        node1 = self.first
        node2 = node1.next
        while node2.next is not None:
            node3 = node2.next
            node2.next = node1
            node1 = node2
            node2 = node3
        else:
            node2.next = node1
        self.first.next = None
        self.first = node2

    def say_goodby(self):
        """
        This Method will remove all the employee with more than 30 years of experience.
        """
        if self.first is None:
            raise IndexError("Link List is Empty")
        while self.first and self.first.experience > 30:
            # Find first element with experience less or equal to 30
            self.first = self.first.next
        if self.first is None:
            return self.first
        temp = self.first
        node = temp.next
        while node is not None:
            if node.experience > 30:
                # Set the last valid node pointer to the next unvalid node
                temp.next = node.next
                node = node.next
            else:
                # Change the last valid node (temp)
                temp, node = node, node.next
        return self.first

    def get_employee(self, employee_id: int):
        """
        Return Employee object if there is a employee with the given id in list.
        If Employee doesn't exists, Return None
        """
        temp = self.first
        while temp is not None:
            if temp.id == employee_id:
                return temp
            temp = temp.next

    def __len__(self):
        i = 0
        temp = self.first
        while temp is not None:
            temp = temp.next
            i += 1
        return i

    def __iter__(self):
        self._node = self.first
        return self

    def __next__(self):
        node = self._node
        while node is not None:
            self._node = node.next
            return node
        raise StopIteration
