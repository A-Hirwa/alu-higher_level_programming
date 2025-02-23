#!/usr/bin/python3
'''Creating a new class rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class'''
    def __init__(self, width, height):
        '''initialize width and height'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''implementing area'''
        return self.__width * self.__height

    def __str__(self):
        '''string representation'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
