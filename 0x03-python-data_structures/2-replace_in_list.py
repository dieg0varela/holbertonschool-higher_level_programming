#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    i = 0
    for num in my_list:
        if i == idx:
            my_list[i] = element
            return (my_list)
        i = i + 1
    return (my_list)
