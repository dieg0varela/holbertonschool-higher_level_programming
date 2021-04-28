#!/usr/bin/python3
a = 0;
for c in reversed(range(97, 123)):
    if a == 1:
        c = c -32
        a = 0
    else:
        a = 1
    print("{:c}".format(c), end='')
