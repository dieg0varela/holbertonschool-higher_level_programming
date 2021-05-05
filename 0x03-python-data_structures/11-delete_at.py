#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return (my_list)
    i = 0
    for num in my_list:
        if i == idx:
            del my_list[i]
            return (my_list)
        i = i + 1
    return (my_list)
