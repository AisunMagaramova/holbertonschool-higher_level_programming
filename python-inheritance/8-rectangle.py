#!/usr/bin/python3


"""
This module contains the BaseGeometry and Rectangle classes.

The BaseGeometry class provides basic geometric operations, including
a method to validate integer values and a method for calculating the area
(which is not implemented in BaseGeometry itself).

The Rectangle class inherits from BaseGeometry and represents a rectangle
with a width and height. It validates the width and height, calculates the
area of the rectangle, and returns a string representation of the rectangle.
"""


class BaseGeometry:
    """
    A base class for geometry shapes.
    """

    def area(self):
        """
        Raises an Exception if this method is not implemented by an inherited class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the value is a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height and validates them.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width} - {self.__height}"
