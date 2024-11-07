#!/usr/bin/python3
'''Creating a new class rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
      '''Square class'''
      def __init__(self, size):
          '''initializing size'''
          self.integer_validator("size", size)
          super().__init__(size, size)
          self.__size = size
      
      def area(self):
          """Area of Square"""
          return self.__size ** 2

      def __str__(self):
          """Returns [Square] <width>/<height>."""
          return super().__str__()
