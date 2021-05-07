#!/usr/bin/python3
def weight_average(my_list=[]):
    div = 0
    res = 0
    if my_list:
        for i in my_list:
            res += (i[0] * i[1])
            div += i[1]
        return (res / div)
    else:
        return (0)
