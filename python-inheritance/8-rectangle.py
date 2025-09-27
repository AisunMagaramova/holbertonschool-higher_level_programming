#!/usr/bin/python3


"""
This module contains a function 'is_same_class' that checks if an object
is exactly an instance of the specified class.
"""

class BaseGeometry:
    """
    A base class for geometry-related shapes and operations.
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
