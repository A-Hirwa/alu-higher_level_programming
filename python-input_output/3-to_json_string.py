#!/usr/bin/python3
"""
3-to_json_string.py

This module has a function that converts a string to JSON
"""


import json

def to_json_string(my_obj):
    """
    This functions converts a string to JSON

    Args:
        my_obj: the string to convert
    """
    result = json.loads(my_obj)
    return result
