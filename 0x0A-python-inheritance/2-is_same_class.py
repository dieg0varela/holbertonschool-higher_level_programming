#!/usr/bin/python3
'''Is_Same_Class Module'''


def is_same_class(obj, a_class):
    '''Is_same_class Class'''
    temp = type(obj)
    return (temp is a_class)
