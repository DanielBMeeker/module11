"""
Program: hourly_employee.py
Author: Daniel Meeker
Date: 7/8/2020

This program demonstrates inheritance by using the employee base class
and having two sub classes inherit from it. This is the hourly employee class
"""
from class_definitions.employee import Employee
import datetime
import locale  # to make formatting the currency a lot easier
locale.setlocale(locale.LC_ALL, '')


class HourlyEmployee(Employee):
    """
    Hourly Employee Class
    """
    def __init__(self, last_name, first_name, address, phone_number, start_date, hourly_pay):
        """
        Constructor for Hourly Employee
        :param last_name: required
        :param first_name: required
        :param address: required
        :param phone_number: required
        :param start_date: required
        :param hourly_pay: required
        """
        super().__init__(last_name, first_name, address, phone_number)
        self._start_date = start_date
        self._hourly_pay = hourly_pay

    def give_raise(self):
        """
        Adds $2.00 an hour to employee pay
        :return: new hourly pay
        """
        bonus = 2
        self._hourly_pay += bonus
        return self._hourly_pay

    def display(self):
        """
        Creates a nice, well-formatted output string
        :return: a string
        """
        date = self._start_date.strftime("%m-%d-%Y")
        pay = locale.currency(self._hourly_pay, True, True)
        return (super().display() + "\n{self._phone_number} \nHourly Pay: ".format(self=self)
                + pay + " per hour \nStart Date: ".format(self=self) + str(date))

    def __str__(self):
        """
        Overrides str function to make it more descriptive
        :return: a string
        """
        date = self._start_date.strftime("%m-%d-%Y")
        pay = locale.currency(self._hourly_pay, True, True)
        return (super().__str__() + "\n{self._phone_number} \nHourly Pay: ".format(self=self)
                + pay + " per hour \nStart Date: ".format(self=self) + str(date))

    def __repr__(self):
        """
        Overrides repr function to mimic the constructor of the class
        :return:
        """
        return super().__repr__() + ", ({self._start_date}), {self._hourly_pay})".format(self=self)


if __name__ == '__main__':
    today = datetime.date.today()
    employee2 = HourlyEmployee("Meeker", "Daniel", '123 Fake St, Des Moines, Iowa', '515-555-5555', today, 10.00)
    print(employee2.display())
    employee2.give_raise()
    print(employee2.display())
    print(repr(employee2))
    print(employee2)
    del employee2
