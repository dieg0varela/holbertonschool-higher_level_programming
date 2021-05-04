#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    i = 0
    new_list = []
    if idx <= (len(my_list) - 1):
        for num in my_list:
            new_list.append(num)
            if i == idx:
                new_list[i] = element
            i = i + 1
        return (new_list)
    return (my_list)
