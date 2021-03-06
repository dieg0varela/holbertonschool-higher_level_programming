#!/usr/bin/python3
"""Module to add 2  integers"""


def add_integer(a, b=98):
    """Funtion to add 2 integers"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, int) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False:
        raise TypeError("b must be an integer")

    res = int(a) + int(b)
    return (res)
