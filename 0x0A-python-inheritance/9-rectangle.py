#!/usr/bin/python3
'''Rectangle Module'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle Class'''
    def __init__(self, width, height):
        '''Init Function'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Area Function'''
        return (self.__width * self.__height)

    def __str__(self):
        '''Str Function'''
        res = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return (res)
