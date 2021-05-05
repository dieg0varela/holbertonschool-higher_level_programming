#!/usr/bin/python3
def max_integer(my_list=[]):
    pan = my_list[0]
    for i in my_list:
        if i > pan:
            pan = i
    return (pan)
