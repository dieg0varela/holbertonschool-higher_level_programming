#!/usr/bin/python3
'''Append Write Module'''


def append_write(filename="", text=""):
    '''append_write function'''
    with open(filename, "a") as f:
        res = f.write(text)
    f.closed
    return (res)
