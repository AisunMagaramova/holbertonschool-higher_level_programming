#!/usr/bin/python3
"""Kvadrat sinfini təyin edən modul."""


class Square:
    """Kvadrat obyektini təyin edir."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Kvadratın ölçüsünü qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin edir və yoxlayır."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Kvadratın mövqeyini qaytarır."""
        return self.__position

    @position.setter
    def position(self, value):
        """Kvadratın mövqeyini təyin edir və yoxlayır."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı '#' ilə çap edir, mövqeyə uyğunlaşdıraraq."""
        if self.__size == 0:
            print()
            return

        # yuxarıdan boş sətir
        for _ in range(self.__position[1]):
            print()

        # hər sətir üçün: boşluq + #
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
