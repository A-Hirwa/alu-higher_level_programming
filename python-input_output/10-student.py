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
        if type(attrs) == list:
            attr_dict = {}
            for i in range(len(attrs)):
                if attrs[i] in self.__dict__:
                    attr_dict[attrs[i]] = self.__dict__[attrs[i]]
            return attr_dict
        else:
            return self.__dict__
