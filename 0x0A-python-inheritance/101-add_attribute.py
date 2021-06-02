#!/usr/bin/python3
'''Advanced task'''


class add_attribute:
    '''Add_attribute Class'''
    def __init__(self, obj, name, val):
        '''Function'''
        lista = dir(obj)
        if "__dict__" in lista:
            setattr(obj, name, val)
        else:
            raise TypeError("can't add new attribute")
