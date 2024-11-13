#!/usr/bin/python3
"""
10-student.py

This module has a student class and a function to return attributes
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

    def to_json(self, attrs=None):
        """
        function returns dictionary representation of a class

        Args:
            self
        """
        if all(isinstance(attr, str) for attr in attrs):
            if attr in self.__dict__:
                print(attr)
        return attrs
