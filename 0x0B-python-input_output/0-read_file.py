#!/usr/bin/python3
'''Read Module'''


def read_file(filename=""):
    '''read_file Function'''
    with open(filename, "r") as f:
        readed = f.read()
    f.closed
    print(readed, end='')
