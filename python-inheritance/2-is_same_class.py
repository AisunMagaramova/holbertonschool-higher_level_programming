#!/usr/bin/python3

def is_same_class(obj, a_class):
    """ Function that checks if the object is exactly an instance of the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to check against.

    Returns:
    bool: True if the object is exactly an instance of the specified class, 
          False otherwise.
    
    Example:
    >>> is_same_class(5, int)
    True
    >>> is_same_class(5, str)
    False"""

    return type(obj) is a_class
    