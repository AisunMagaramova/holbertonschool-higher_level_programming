#!/usr/bin/python3
"""
This module contains the BaseGeometry, Rectangle, and Square classes.

BaseGeometry provides basic geometric operations, including a method to validate integer values
and a method for calculating the area (which is not implemented in BaseGeometry itself).

Rectangle inherits from BaseGeometry and represents a rectangle with a width and height.
The width and height are validated and must be positive integers.

Square inherits from Rectangle. It represents a square, where both the width and height are equal,
and the size is validated to be a positive integer.
"""

class BaseGeometry:
    """
    A base class with basic geometric operations.
    """

    def area(self):
        """
        Raises an Exception if area() is not implemented in subclass.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates if the value is a positive integer.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, which inherits from BaseGeometry.
    """
    
    def __init__(self, width, height):
        """
        Initializes a rectangle object with width and height.
        Both width and height must be positive integers.
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width  # Set the width
        self.__height = height  # Set the height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class representing a square, which inherits from Rectangle.
    The size of the square is validated and used as both the width and height.
    """

    def __init__(self, size):
        """
        Initializes a square object with size.
        The size must be a positive integer and is used for both width and height.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
