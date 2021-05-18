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
