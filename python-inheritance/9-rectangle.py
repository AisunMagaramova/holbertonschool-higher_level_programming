#!/usr/bin/python3


"""
This module contains a function 'is_same_class' that checks if an object
is exactly an instance of the specified class.
"""


from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle sinifi BaseGeometry sinifindən irs alır və düzbucaqlı obyektini təmsil edir.
    
    width: düzbucaqlının enini saxlayır
    height: düzbucaqlının hündürlüyünü saxlayır
    """

    def __init__(self, width, height):
        """
        Düzbucaqlının enini və hündürlüyünü ilkinləşdirir və hər ikisini yoxlayır.
        
        width: Düzbucaqlının eni (tam ədəd)
        height: Düzbucaqlının hündürlüyü (tam ədəd)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Düzbucaqlının sahəsini hesablayır.
        
        Returns:
            int: Düzbucaqlının sahəsi (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Düzbucaqlının mətn formatında nümayişini qaytarır.
        
        Returns:
            str: "[Rectangle] <width>/<height>"
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
