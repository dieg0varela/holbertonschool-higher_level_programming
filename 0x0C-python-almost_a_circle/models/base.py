#!/usr/bin/python3
'''Base Module'''
import json


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Init Method'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            ret = json.dumps(list_dictionaries)
            return (ret)

    @classmethod
    def save_to_file(cls, list_objs):
        name = cls.__name__ + ".json"
        if list_objs is None:
            res = []
        else:
            res = []
            for obj in list_objs:
                res.append(obj.to_dictionary())
        with open(name, "w") as f:
            f.write(Base.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            res = []
            return (res)
        else:
            res = json.loads(json_string)
            return (res)
