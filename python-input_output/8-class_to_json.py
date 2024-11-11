#!/usr/bin/python3
"""
8-class_to_json.py

This module has a function that returns the dictionary description
"""


def class_to_json(obj):
    """
    This function returns a dictionary description

    Args:
        obj: the instance of the class
    """
    return obj.__dict__
