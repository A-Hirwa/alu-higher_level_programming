#!/usr/bin/python3
"""
2-append_write.py

This module has a function that appends a string to a file
"""


def append_write(filename="", text=""):
    """
    This function adds a string to a file

    Args:
        filename: the file to add the string to
        text: the string being added
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        f.append(text)
    return len(text)
