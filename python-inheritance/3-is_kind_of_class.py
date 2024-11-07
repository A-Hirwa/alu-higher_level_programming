#!/usr/bin/python3
'''Creates a function that tests if objects are instances of a class'''


def is_kind_of_class(obj, a_class):
    '''Function returns true if obj is an instance and false if not
    Args:
        obj: object to check
        a_class: class to check
    '''
    x = isinstance(obj, a_class)
    return x
