#!/usr/bin/python3
"""
My first square
"""

class Square:
    """
    this class creates the square object
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initiazation
        size (int):
            size of the square
        """
        self.size = size
        self.position = position


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
            return
        print("\n" * self.__position[1], end='')
        for i in range(self.__size):
            print(" " * self.__position[0], end='')
            print('#' * self.__size)

    @property
    def position(self):
        """
        Coordinates of a square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Coordinates of a square
        """
        if not isinstance(value, tuple)\
            or len(value) != 2\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
