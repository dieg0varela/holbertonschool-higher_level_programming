#!/usr/bin/python3
'''Inherits_From Module'''


def inherits_from(obj, a_class):
    '''Inherits_From function'''
    temp = type(obj) != a_class
    return (issubclass(type(obj), a_class) and temp)
