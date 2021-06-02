#!/usr/bin/python3
'''Save to json File Module'''


def save_to_json_file(my_obj, filename):
    '''save_to_json_file Function'''
    import json
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
    f.closed
