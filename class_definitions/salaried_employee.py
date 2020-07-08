"""
Program: salaried_employee.py
Author: Daniel Meeker
Date: 7/8/2020

This program demonstrates inheritance by using the employee base class
and having two sub classes inherit from it. This is the salaried employee class
"""
from class_definitions.employee import Employee
import datetime
import locale  # to make formatting the currency a lot easier
locale.setlocale(locale.LC_ALL, '')


class SalariedEmployee(Employee):
    """
    Salaried Employee Class
    """
    def __init__(self, last_name, first_name, address, phone_number, start_date, salary):
        """
        Constructor for Salaried Employee
        :param last_name: required
        :param first_name: required
        :param address: required
        :param phone_number: required
        :param start_date: required
        :param salary: required
        """
        super().__init__(last_name, first_name, address, phone_number)
        self._start_date = start_date
        self._salary = salary

    def give_raise(self):
        """
        When called this method adds $5,000 to the employee pay
        :return: new hourly pay
        """
        bonus = 5000
        self._salary += bonus
        return self._salary

    def display(self):
        """
        Creates a nice, well-formatted output string
        :return: a string
        """
        date = self._start_date.strftime("%m-%d-%Y")
        pay = locale.currency(self._salary, True, True)
        return (super().display() + "\n{self._phone_number} \nSalary: ".format(self=self)
                + pay + "\nStart Date: ".format(self=self) + str(date))

    def __str__(self):
        """
        Overrides the str function to make it more descriptive
        :return:
        """
        date = self._start_date.strftime("%m-%d-%Y")
        pay = locale.currency(self._salary, True, True)
        return (super().__str__() + "\n{self._phone_number} \nSalary: ".format(self=self)
                + pay + "\nStart Date: ".format(self=self) + str(date))

    def __repr__(self):
        """
        Overrides the repr function so that it mimics the class constructor
        :return:
        """
        return super().__repr__() + ", ({self._start_date}), + {self._salary})".format(self=self)


if __name__ == '__main__':
    today = datetime.date.today()
    employee1 = SalariedEmployee("Meeker", "Daniel", '123 Fake St, Des Moines, Iowa', '515-555-5555', today, 40000)
    print(employee1.display())
    employee1.give_raise()
    print(employee1.display())
    print(repr(employee1))
    print(employee1)
    del employee1
