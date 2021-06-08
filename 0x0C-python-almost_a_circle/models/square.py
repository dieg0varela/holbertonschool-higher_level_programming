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

    def update(self, *args, **kwargs):
        '''Update Method'''
        if args is not None and len(args) != 0:
            cont = len(args)
            if cont >= 1:
                self.id = args[0]
            if cont >= 2:
                self.size = args[1]
            if cont >= 3:
                self.x = args[2]
            if cont >= 4:
                self.y = args[3]
        elif kwargs is not None:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs.get(i)
                elif i == "size":
                    self.size = kwargs.get(i)
                elif i == "x":
                    self.x = kwargs.get(i)
                elif i == "y":
                    self.y = kwargs.get(i)

    def to_dictionary(self):
        '''To_dictionary Method'''
        res = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return (res)


    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
