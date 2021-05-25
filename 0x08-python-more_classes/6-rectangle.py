#!/usr/bin/python3
"""Define Class Rectangle"""


class Rectangle:
    """Class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init Method Rectangle"""
        if (isinstance(width, int) is False):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = width
        if (isinstance(height, int) is False):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Str Method"""
        x = 0
        y = 0
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return (rect)
        for y in range(self.__height):
            for x in range(self.__width):
                rect += "#"
            if y != (self.__height - 1):
                rect += "\n"
        return (rect)

    def __repr__(self):
        """Repr Method"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """del Method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Area Calcuation"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter calculation"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        perimeter = (self.__height * 2) + (self.__width * 2)
        return (perimeter)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
