"""
Program: employee.py
Author: Daniel Meeker
Date: 7/8/2020

This will serve as the base class for the hourly employee and salaried
employee classes.
"""


class Employee:
    """Employee Class """
    # Constructor
    def __init__(self, last_name, first_name, address,
                 phone_number):
        """
        Constructor for the Employee class
        :param last_name: string
        :param first_name: string
        :param address: string
        :param phone_number: string
        """
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(last_name) and name_characters.issuperset(first_name)):
            raise ValueError
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number

    # Class functions
    def display(self):
        """
        This function organizes all the information from the object
        into a nicely formatted output string
        :return: a string
        """
        address_array = str(self._address).split(',')
        street = address_array[0]
        city = address_array[1]
        state = address_array[2]
        return (str(self._first_name) + " " + str(self._last_name) + "\n"
                + str(street).strip() + '\n' + str(city).strip() + ', ' + str(state).strip())

    def __str__(self):
        """
        Overrides the built-in string function to provide a basic string describing the class object
        :return: a string giving a little information about the object
        """
        return "Employee with last name " + str(self._last_name) + ', first name ' + str(self._first_name)

    def __repr__(self):
        """
        Overrides the built-in repr function.
        :return: a string that contains all the information needed to recreate the object
        """
        return ("{self.__class__.__name__}('{self._last_name}', '{self._first_name}',"
                " '{self._address}', '{self._phone_number}'".format(self=self))


if __name__ == '__main__':
    pass
