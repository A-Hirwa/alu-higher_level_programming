#!/usr/bin/python3
"""
9-student.py

This module has a class with a function that 
returns a dictionary representation of the class
"""


class Student:
    """
    This is a class that defines a student

    attributes:
                first_name
                last_name
                age
    """
    def __init__(self, first_name, last_name, age):
        """
        initializing class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function returns dictionary representation of a class

        Args:
            self
        """
        return self.__dict__
