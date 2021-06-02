#!/usr/bin/python3
'''To JSON String Module'''


def to_json_string(my_obj):
    '''to_json_string Function'''
    import json
    res = json.dumps(my_obj)
    return (res)
