#!/usr/bin/python3
'''Rectangle Module'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle Class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Init Method'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''Str Method'''
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        '''Update Method'''
        if args is not None:
            cont = len(args)
        if cont == 1:
            self.id = args[0]
        elif cont == 2:
            self.id = args[0]
            self.width = args[1]
        elif cont == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        elif cont == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif cont == 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

    def area(self):
        '''Area Method'''
        return (self.height * self.width)

    def display(self):
        '''Display Method'''
        x_spaces = " " * self.x
        for y_spaces in range(self.y):
            print()
        for y in range(self.height):
            print(x_spaces, end='')
            for x in range(self.width):
                print("#", end='')
            print()

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
