#!/usr/bin/python3
'''Student Module'''


class Student:
    '''Student Class'''
    def __init__(self, first_name, last_name, age):
        '''Init function'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''to_json Function'''
        dicty = {"first_name": self.first_name, "last_name": self.last_name,
                 "age": self.age}
        return (dicty)
