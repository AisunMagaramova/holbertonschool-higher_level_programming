#!/usr/bin/python3


"""
This module contains a function 'is_same_class' that checks if an object
is exactly an instance of the specified class.
"""


class BaseGeometry:
    """
    A base class for geometry-related shapes and operations.
    This class is still empty, but we will add the area() method.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'
        when called, indicating that the method should be implemented by
        subclasses.
        """
        raise Exception("area() is not implemented")
