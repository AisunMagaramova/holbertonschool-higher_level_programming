#!/usr/bin/python3
"""Kvadrat sinfini teyin eden modul."""


class Square:
    """Kvadrat obyektini teyin edir."""

    def __init__(self, size=0):
        """Private size ile kvadrat yaradılıre yoxlanılır."""
        self.size = size

    @property
    def size(self):
        """Size atributunun dəyərini qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size atributunu yenileyir, yoxlayır."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın saesini qaytarır."""
        return self.__size ** 2
