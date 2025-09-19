#!/usr/bin/python3
class Square:
    """
    Kvadrat sinifi, size atributu ile olcusunu teyin edirik.
    """


    def __init__(self, size):
        """
        Yeni kvadrat sinifi yarat.
        :param size, kvadartin olcusu
        """
        self.__size = size

        def size(self):
            return self.__size

        My_square = Square(3)
        print(my_square.size)
        print(my_square.__size)
