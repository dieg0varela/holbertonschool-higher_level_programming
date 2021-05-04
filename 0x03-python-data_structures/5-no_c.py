#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new = new + c
        i = i + 1
    return (new)
