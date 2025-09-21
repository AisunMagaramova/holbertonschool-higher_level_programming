#!/usr/bin/python3
"""Kvadrat sinifini teyin eden modul."""


class Square:
    """Kvadrati teyin eidr."""

    def __init__(self, size=0):
        """Pirivate size ile kvadrat yaradilir yoxlanili."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
