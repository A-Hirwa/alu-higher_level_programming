#!/usr/bin/python3
'''Creates a function that tests if objects are instances of a class'''


def is_same_class(obj, a_class):
    '''Function returns true if obj is an instance and false if not
    
    Args:
        obj: object to check
        a_class: class to check
    '''
    return type(obj) is a_class
