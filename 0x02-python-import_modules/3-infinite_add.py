#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = (len(argv))
    res = 0
    for pichu in range(1, argc):
        res = res + int(argv[pichu])
    print("{:d}".format(res))
