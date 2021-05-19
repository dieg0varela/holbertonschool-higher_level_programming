#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Init Method load size"""
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        if ((isinstance(position, tuple) is False) or (len(position) != 2)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(position[0], int) is False or position[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(position[1], int) is False or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Area calculation"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square of your size"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(" ", end='')
                for y in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((isinstance(value, tuple) is False) or (len(value) != 2)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(value[0], int) is False or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(value[1], int) is False or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
