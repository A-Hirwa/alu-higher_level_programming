#!/usr/bin/python3
'''Creates a function that tests if objects are subclasses of a class'''


def inherits_from(obj, a_class):
    '''Function returns true if obj is an sub class and false if not
    Args:
        obj: object to check
        a_class: class to check
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
