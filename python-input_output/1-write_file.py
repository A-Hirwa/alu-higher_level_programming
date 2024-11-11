#!/usr/bin/python3
"""
1-write_file.py

This module as a function that adds a string to a file
"""


def write_file(filename="", text=""):
    """
    This function adds a string to a file

    Args:
        filename: the file added to
        text: the string added to the file
    """
    with open(filename, mode="w", encoding="UTF-8") as file:
        file.write(text)
        return len(text)
