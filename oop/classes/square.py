#!/usr/bin/python3
"""
My first square
"""

class Square:
    """
    this class creates the square object
    """

    def __init__(self, size=0):
        """
        initiazation
        size (int):
            size of the square
        """
        self.size = size

    def area(self):
        """
        Area of a square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Access and update private attribute
        """
        return self.__size

    @size.setter
    def size(self, s):
        """
        Access and update private attribute
        """
        if not isinstance(s, int):
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
        self.__size = s

    def my_print(self):
        """Printing a square """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print('#' * self.__size)
