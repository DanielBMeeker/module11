"""
Program: Student
Author: Daniel Meeker
Date: 7/7/2020

This program demonstrates class objects by using a person class
from the instructor that has been modified by Daniel Meeker, to help
create the student class. It includes a change major function, a update gpa
function and a display function. As well as str and repr functions.
"""
from datetime import date
from class_definitions import person as p

# Moved the list of majors out here so that it could be used by both the constructor and the change major function
majors = ('BIS-OOP', 'CIS', 'Web Development', 'Network Security')


class Student:
    """
    Student Class
    """
    def __init__(self, person, major, start_date, gpa=0.0):
        """
        This is the Student Constructor
        :param person: a Person class object
        :param major: required
        :param start_date: required
        :param gpa: optional
        """
        if major not in majors:
            raise ValueError("Major must be one of the available majors")
        if not isinstance(gpa, float) or not 0.0 <= gpa <= 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")
        self.person = person
        self.major = major
        self.start_date = start_date
        self.gpa = gpa

    def change_major(self, major):
        """
        This function will change the major of the Student object
        it includes validation.
        :param major: the new major
        :return: no return
        """
        if major not in majors:
            raise ValueError("Major not changed: \nMajor must be in available majors list.")
        else:
            self.major = major

    def update_gpa(self, gpa):
        """
        This function will change the gpa of the Student object
        it includes validation
        :param gpa: required - the new gpa
        :return: no return
        """
        if not isinstance(gpa, float) or not 0.0 <= gpa <= 4.0:
            raise ValueError("GPA not updated: \nGPA must be between 0.0 and 4.0")
        else:
            self.gpa = gpa

    def display(self):
        """
        Displays all the relevant information of the Student object
        :return: a string
        """
        return ("Student: {self.person} \nMajor: {self.major} "
                "\nStart date: {self.start_date.month}-{self.start_date.day}-{self.start_date.year}"
                " \nGPA: {self.gpa}".format(self=self))

    def __str__(self):
        """
        Displays all the relevant information of the Student object
        :return: a string
        """
        return ("Student: {self.person} \nMajor: {self.major} "
                "\nStart date: {self.start_date.month}-{self.start_date.day}-{self.start_date.year}"
                " \nGPA: {self.gpa}".format(self=self))

    def __repr__(self):  # I am not sure the best way to format the date to make it usable in the repr.
        """
        Used to mimic the constructor
        :return: a string
        """
        return ("{self.__class__.__name__}(p.".format(self=self) + repr(self.person)
                + ", '{self.major}', ({self.start_date.year}, {self.start_date.month}, "
                  "{self.start_date.day}), {self.gpa}".format(self=self))


if __name__ == '__main__':
    student_name = p.Person('Meeker', "Daniel")
    student_major = "BIS-OOP"
    student_start = date.today()
    student_GPA = 3.9
    try:  # This block should all work fine
        student1 = Student(student_name, student_major, student_start, student_GPA)
        print(student1.display())
        student1.change_major('CIS')
        print(student1.display())
        student1.update_gpa(3.5)
        print(student1.display())
    except ValueError as e:
        print(e)
    try:  # Should raise an error because it's not an available major
        student1.change_major('Video Game Development')
        print(student1.display())
    except ValueError as e:
        print(e)
    try:  # Should raise an error because its not an acceptable GPA range
        student1.update_gpa(4.5)
        print(student1.display())
    except ValueError as e:
        print(e)
    print(repr(student1))
