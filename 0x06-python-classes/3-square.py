#!/usr/bin/python3
"""
This is still the module's documentation
Still working on the square class
add a little more
"""


class Square:
    """This is the object documentation"""
    __size = 0

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Return area of Square """
        return (self.__size * self.__size)
