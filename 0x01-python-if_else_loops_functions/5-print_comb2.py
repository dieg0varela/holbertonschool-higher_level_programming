#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("0", end='')
    print("{:d}".format(i), end='')
    if i != 99:
        print(", ", end='')
print()
