#!/usr/bin/python3
'''Adding value validator to the class'''


class BaseGeometry:
    '''Base class'''
    def area(self):
        '''raises an area exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
