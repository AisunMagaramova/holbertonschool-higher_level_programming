#!/usr/bin/python3
"""
Kvadrat sinifi, size atributu ile olcusunu teyin edirik.
"""

class Square:
    def __init__(self, size):
        """
        Yeni kvadrat sinifi yarat.
        :param size: kvadratın ölçüsü
        """
        self.__size = size

    @property
    def size(self):
        """
        size atributunun getter metodu.
        """
        return self.__size


if __name__ == "__main__":
    my_square = Square(3)
    print(my_square.size)
