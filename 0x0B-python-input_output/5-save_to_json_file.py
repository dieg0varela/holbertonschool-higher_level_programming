#!/usr/bin/python3
'''Save to json File Module'''


def save_to_json_file(my_obj, filename):
    '''save_to_json_file Function'''
    import json
    obj_json_format = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(obj_json_format)
    f.closed
