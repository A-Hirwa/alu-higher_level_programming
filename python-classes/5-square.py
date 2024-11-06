#!/usr/bin/python3
""" Square class to represent a class"""


class Square:
    """Define square class with size greater than 0"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    @property
    def size(self):
        """Return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
          
    def area(self):
        """Return area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square"""
        for i in range(self.__size):
            if self.__size == 0:
                print("")
            else:
                print("#" * self.__size)
