#!/usr/bin/python3


"""
This module contains a function 'is_same_class' that checks if an object
is exactly an instance of the specified class.
"""


from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inherits from BaseGeometry.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Methods:
    area(): Returns the area of the rectangle.
    """
    
    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height. Both attributes are validated
        to be positive integers.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
       self.__height = height 
    
    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
        int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height
