#!/usr/bin/python3
"""" Kvadrat sinidfini teyin eden modul. """


class Square:
    """Kvadrat obyektini teyin edir."""

    def __init__(self, size=0):
        """Pirivate size kvadrat yaradilir ve yoxlanilir."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratin sahesini aytarir."""
        return self.__size ** 2
