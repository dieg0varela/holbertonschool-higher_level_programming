#!/usr/bin/python3
'''Class to json Module'''


def class_to_json(obj):
    '''class_to_json Function'''
    import json
    return (json.dumps(obj.__dict__))
