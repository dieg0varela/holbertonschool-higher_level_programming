#!/usr/bin/python3
'''Load from json file Module'''


def load_from_json_file(filename):
    '''load_from_json_file'''
    import json
    with open(filename, "r") as f:
        json_loaded = f.read()
    f.closed
    obj = json.loads(json_loaded)
    return (obj)
