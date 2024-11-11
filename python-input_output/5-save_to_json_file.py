#!/usr/bin/python3
"""
5-save_to_json_file.py

This module has writes an object to a JSON text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a JSON file

    Args:
        my_obj: the object to add to the file
        filename: the name of the file
    """
    with open(filename,"w") as f:
        json.dump(my_obj, f)
