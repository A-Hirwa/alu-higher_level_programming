#!/usr/bin/python3
def read_file(filename=""):
    """
    reads a filename

    Args:
        filename: the file to read
    """
    with open("filename", encoding="UTF-8") as myfile:
        result = myfile.read()
        print({}.format(result))
