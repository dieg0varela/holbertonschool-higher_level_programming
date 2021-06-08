#!/usr/bin/python3
'''Square Module'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square Class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Init Method'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Str Method'''
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
