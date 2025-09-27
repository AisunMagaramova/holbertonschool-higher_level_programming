#!/usr/bin/python3


from 7-base_geometry import BaseGeometry
"""
This module contains a class 'Rectangle' that represents a rectangle.
It inherits from BaseGeometry.
"""


class BaseGeometry:
    """
    A class used as a base for geometric shapes.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'
        when called, indicating that the method should be implemented by
        subclasses.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Parameters:
        name (str): The name of the attribute being validated.
        value (int): The value of the attribute to validate.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

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
    
    def __str__(self):
        """
        Return a string representation of the Rectangle object.
        """
        return f"[Rectangle] {self.__width} - {self.__height}"

