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


# Sinifdən obyekt yaradılması və çap edilməsi modul səviyyəsində
if __name__ == "__main__":
    my_square = Square(3)
    print(my_square.size)        # 3
    # print(my_square.__size)    # Bu xəta verər, gizli atributa birbaşa müraciət olmaz
