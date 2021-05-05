#!/usr/bin/python3
def max_integer(my_list=[]):
    pan = 0
    for i in my_list:
        if i > pan:
            pan = i
    return (pan)
