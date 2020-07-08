"""
Program: student_inheritence
Author: Daniel Meeker
Date: 7/8/2020

This program demonstrates inheritance with class objects.
Student is a child class of person so the last name and first
name from the student constructor gets passed to the person constructor
which validates them.
"""
from datetime import date
from class_definitions.person import Person

# Moved the list of majors out here so that it could be used by both the constructor and the change major function
majors = ('Computer Science', 'Computer Engineering', 'BIS-OOP', 'CIS', 'Web Development', 'Network Security')


class Student(Person):
    """
    Student Class
    """
    def __init__(self, student_id, last_name, first_name, major='Computer Science', gpa=0.0):
        """
        This is the Student Constructor
        :param student_id: required
        :param last_name: required
        :param first_name: required
        :param major: optional - defaults to Computer Sciecne
        :param gpa: optional - defaults to 0.0
        """
        super().__init__(last_name, first_name)
        if major not in majors:
            raise ValueError("Major must be one of the available majors")
        if not isinstance(gpa, float) or not 0.0 <= gpa <= 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")
        if len(str(student_id)) != 9 and not isinstance(student_id, int) or (str(student_id)[:3]) != '900':
            raise ValueError("Student ID must be a number beginning with 900 and be 9 digits long")
        self._student_id = student_id
        self._major = major
        self._gpa = gpa

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
            self._major = major

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
            self._gpa = gpa

    def display(self):
        """
        Displays all the relevant information of the Student object
        :return: a string
        """
        return ('{self._last_name}, {self._first_name}:({self._student_id}) '
                '{self._major} gpa: {self._gpa}'.format(self=self))

    def __str__(self):
        """
        Displays all the relevant information of the Student object
        :return: a string
        """
        return ("Student: {self._last_name}, {self._first_name} "
                "\nStudent ID: {self._student_id}"
                "\nMajor: {self._major} "
                "\nGPA: {self._gpa}".format(self=self))

    def __repr__(self):  # I am not sure the best way to format the date to make it usable in the repr.
        """
        Used to mimic the constructor
        :return: a string
        """
        return ("{self.__class__.__name__}({self._student_id}, "
                "'{self._last_name}', '{self._first_name}', "
                "'{self._major}', {self._gpa})".format(self=self))


if __name__ == '__main__':
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    print(my_student)
    print(repr(my_student))
    del my_student
