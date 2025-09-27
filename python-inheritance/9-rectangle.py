#!/usr/bin/python3

class BaseGeometry:
    """
    A base class with basic geometric operations
    """
    
    def area(self):
        """
        Raises an Exception if area() is not implemented in subclass
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
    A class representing a rectangle, which inherits from BaseGeometry
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

