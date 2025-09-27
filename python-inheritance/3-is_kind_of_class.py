#!/usr/bin/python3


"""
This module contains a function 'is_same_class' that checks if an object
is exactly an instance of the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Funcn that checks if the object an instance of or if the objectan
    instance of a class that inherited from, the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to check against.

    Returns:
    bool: True if the object instance of or if the object instance of
          a class that inherited from, the specified class, False otherwise.

    Example:
    >>> is_kind_of_class(5, int)
    True
    >>> is_kind_of_class(5, str)
    False
    >>> is_kind_of_class(5, object)
    True
    """
    return isinstance(obj, a_class)


# Test the function
if __name__ == "__main__":
    # Test with an integer object and the int class
    print(is_kind_of_class(5, int))

    # Test with an integer object and the str class
    print(is_kind_of_class(5, str))

    # Test with an integer object and the object class (base class)
    print(is_kind_of_class(5, object))
