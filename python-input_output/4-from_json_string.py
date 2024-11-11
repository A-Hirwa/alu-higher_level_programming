#!/usr/bin/python3
"""
4-from_json_string.py

This module contains a function that converts a JSON string to python
"""


import json


def from_json_string(my_str):
    """
    This function converts JSON string to python

    Args:
        my_str: string to convert
    """
    result = json.loads(my_str)
    return result
