#!/usr/bin/python3


"""
This module contains a function 'is_same_class' that checks if an object
is exactly an instance of the specified class.
"""


def inherits_from(obj, a_class):
    """
    Function that checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (type): The class to check against.

    Returns:
    bool: True if the object is an instance of a class that inherited from
          the specified class, False otherwise.
    
    Example:
    >>> inherits_from(5, int)
    False
    >>> inherits_from(5, object)
    True
    >>> inherits_from(True, int)
    True
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

# Test the function
if __name__ == "__main__":
    # Test with an integer object and the int class
    print(inherits_from(5, int))
    
    # Test with an integer object and the object class (base class)
    print(inherits_from(5, object))
    
    # Test with a boolean object and the int class
    print(inherits_from(True, int))
    
    # Test with a string object and the int class
    print(inherits_from("hello", int))
