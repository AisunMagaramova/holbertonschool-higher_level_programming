def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
    obj: The object whose attributes and methods are to be returned.

    Returns:
    A list containing the names of the attributes and methods of the object.
    """
    return dir(obj)
