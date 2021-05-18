#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Class Square"""
    def __init__(self, new_size=0):
        """Init Method load size"""
        if (isinstance(new_size, int) is False):
            raise TypeError("size must be an integer")
        if (new_size < 0):
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def area(self):
        """Area calculation"""
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if (isinstance(val, int) is False):
            raise TypeError("size must be an integer")
        if (val < 0):
            raise ValueError("size must be >= 0")
        self.__size = val
