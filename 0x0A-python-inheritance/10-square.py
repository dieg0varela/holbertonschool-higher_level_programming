#!/usr/bin/python3
'''Square Module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square Class'''
    def __init__(self, size):
        '''Init function'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
