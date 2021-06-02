#!/usr/bin/python3
'''From json string'''


def from_json_string(my_str):
    '''from_json_string'''
    import json
    obj = json.loads(my_str)
    return (obj)
