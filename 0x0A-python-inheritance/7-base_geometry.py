#!/usr/bin/python3
'''Base Geometry Module'''


class BaseGeometry:
    '''BaseGeometry Class'''
    def area(self):
        '''Area Function'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Integer_Validator Function'''
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
