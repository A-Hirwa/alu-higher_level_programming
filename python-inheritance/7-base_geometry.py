#!/usr/bin/python3
'''Adding value validator to the class'''


class BaseGeometry:
    '''Base class'''
    def area(self):
        '''raises an area exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) == int:
           raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than zero")
