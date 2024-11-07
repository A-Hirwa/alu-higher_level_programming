#!usr/bin/python3
"""function returns class objects and attributes"""


def lookup(obj):
    """Takes obj argument and returns methods and attributes"""
    results = list(dir(obj))
    return results
