#!/usr/bin/python3
"""
6-load_from_json_file.py

This module conatins a function that creates an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    This function creates an object from a JSON file

    Args:
        filename: file to use
    """
    with open(filename, "r") as f:
        result = json.load(f)
    return result
