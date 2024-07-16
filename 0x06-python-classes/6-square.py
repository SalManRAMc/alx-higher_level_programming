#!/usr/bin/python3
"""
This is still the module's documentation
Still working on the square class
add a little more
"""


class Square:
    """This is the object documentation"""
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position = (0, 0)):
        self.size = size
        self.position = position

    @property  # decorator used to indicate a getter
    def size(self):
        return (self.__size)

    @size.setter  # decorator used to indicate a setter for an attribute
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        try:
            self.__position = (value)
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        """ Return area of Square """
        return (self.__size * self.__size)

    def my_print(self):
        i, j, k = 0, 0, 0
        if (self.size > 0):
            while (i < self.size):
                j = 0
                k = 0
                while (j < self.size):
                    while (k < self.position[0]):
                        print("_", end='')
                        k += 1
                    print("#", end='')
                    j += 1
                print()
                i += 1
        else:
            print()
