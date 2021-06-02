#!/usr/bin/python3
'''Write File Module'''


def write_file(filename="", text=""):
    '''Write_file function'''
    with open(filename, "w") as f:
        res = f.write(text)
    f.closed
    return (res)
