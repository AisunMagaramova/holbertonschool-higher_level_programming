#!/usr/bin/python3
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
        Returns the string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width} - {self.__height}"
