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
    A base class for geometric objects.
    Contains a method for validating integer values and a placeholder for the area method.
    """
    
    def integer_validator(self, name, value):
        """
        Validates that the given value is a positive integer.
        Args:
            name (str): The name of the object (e.g., 'width', 'height').
            value (int): The value to be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inherited from BaseGeometry.
    """
    
    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height, validated by integer_validator.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width  # Set the width of the rectangle
        self.__height = height  # Set the height of the rectangle
    
    def area(self):
        """
        Returns the area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle: [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    A class representing a square, inherited from Rectangle.
    """
    
    def __init__(self, size):
        """
        Initializes the square with a given size.
        The size is validated to ensure it's a positive integer.
        """
        self.integer_validator("size", size)  # Validate size
        self.__size = size  # Set the size (both width and height)
        super().__init__(size, size)  # Call the Rectangle's constructor
    
    def area(self):
        """
        Returns the area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square: [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
