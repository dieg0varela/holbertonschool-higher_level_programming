#!/usr/bin/python3
def uppercase(str):
    a = ''
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            a = a + chr(ord(str[i]) - 32)
        else:
            a = a + str[i]
    print(a)
