#!/usr/bin/python3
from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle sinifi BaseGeometry sinifindən irs alır.
    """

    def __init__(self, width, height):
        """
        Rectangle obyekti 'width' və 'height' dəyərləri ilə ilkinləşdirilir.
        Bu dəyərlər 'integer_validator' metodu ilə yoxlanılır.
        """
        self.integer_validator("width", width)  # width dəyərini yoxla
        self.integer_validator("height", height)  # height dəyərini yoxla
        self.__width = width  # width özəlliyini təyin et
        self.__height = height  # height özəlliyini təyin et

    def area(self):
        """
        Rectangle-in sahəsini hesablayır.
        """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width} - {self.__height}"
        