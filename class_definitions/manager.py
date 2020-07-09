"""
Program: manager.py
Author: Daniel Meeker
Date: 7/8/2020

This program demonstrates inheritance by using the person and employee
classes as super classes for the manager class. I chose to use the SalariedEmployee
class instead of the regular employee to save on coding time because it had
more of the fields needed for the manager class.
"""
from class_definitions.salaried_employee import SalariedEmployee
from class_definitions.hourly_employee import HourlyEmployee
from class_definitions.person import Person
import datetime
import locale  # to make formatting the currency a lot easier
locale.setlocale(locale.LC_ALL, '')


class Manager(SalariedEmployee, Person):
    """
    Manager Class - chose to inherit from Salaried Employee rather than regular employee
    because it has more of the necessary fields already in the class
    """
    def __init__(self, last_name, first_name, address,
                 phone_number, start_date, salary,
                 department, direct_reports=()):
        """
        Constructor for Salaried Employee
        :param last_name: required
        :param first_name: required
        :param address: required
        :param phone_number: required
        :param start_date: required
        :param salary: required
        """
        super().__init__(last_name, first_name,
                         address, phone_number,
                         start_date, salary)
        self._department = department
        self._direct_reports = direct_reports

    def give_raise(self):
        """
        When called this method adds $2,000 to the employee pay
        Overrides the function from the salaried employee class
        :return: new hourly pay
        """
        bonus = 2000
        self._salary += bonus
        return self._salary

    def display(self):
        """
        Creates a nice, well-formatted output string
        Overrides the display from salaried_employee but calls
        on the salaried employee display and appends it.
        :return: a string
        """
        employees = ''
        for x in self._direct_reports:
            employees += str(x) + "\n"
        return (super().display() + "\nDepartment: {self._department}"
                                    "\nEmployees Overseen: ".format(self=self) + employees)

    def __str__(self):
        """
        Overrides the str function to make it more descriptive
        :return:
        """
        return (super().__str__() + "\nDepartment: {self._department}"
                                    "\nEmployees Overseen: {self._direct_reports}".format(self=self))

    def __repr__(self):
        """
        Overrides the repr function so that it mimics the class constructor
        :return:
        """
        return (str(super().__repr__())[:-1]
                + ", '{self._department}', {self._direct_reports})".format(self=self))


if __name__ == '__main__':
    today = datetime.date.today()
    employee1 = SalariedEmployee("Peppers", "Joe", '123 Real St, Des Moines, Iowa', '515-515-5151', today, 40000)
    employee2 = HourlyEmployee("Meeker", "Daniel", '123 Fake St, Des Moines, Iowa', '515-555-5555', today, 10.00)
    employees_overseen = (employee1, employee2)
    manager1 = Manager("Meeker", "Daniel", '123 Fake St, Des Moines, Iowa', '515-555-5555', today, 40000, "Sales", employees_overseen)
    print(manager1.display())  # Calls the display from the manager class which calls the display from the Salaried Employee class
    manager1.give_raise()
    print(manager1.display())
    print(repr(manager1))
    print(manager1)
    del manager1, employee1, employee2
