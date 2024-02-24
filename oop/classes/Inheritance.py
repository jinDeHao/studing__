#!/usr/bin/env python3
"""
inheritance
"""



class MyList(list):
    """
    1. My list
    """
    def print_sorted(self):
        """method that print sorted list"""
        print(sorted(self))

def is_same_class(obj, a_class):
    """
    2. Exact same object
    """
    return type(obj) == a_class


def is_kind_of_class(obj, a_class):
    """
    3. Same class or inherit from
    """
    return isinstance(obj, a_class)


def inherits_from(obj, a_class):
    """
    4. Only sub class of
    """
    return type(obj) != a_class and isinstance(obj, a_class)


class BaseGeometry:
    """
    5. Geometry module
    """
    def area(self):
        """
        6. Improve Geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        7. Integer validator
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    8. Rectangle
    """
    def __init__(self, width, height):
        """
        8. Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        9. Full rectangle
        """
        return self.__width * self.__height
