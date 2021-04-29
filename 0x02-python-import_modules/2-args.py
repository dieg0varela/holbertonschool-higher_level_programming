#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = (len(argv) - 1)
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argumet:".format(argc))
        print("{:d}: {}".format(argc, argv[argc]))
    else:
        print("{:d} arguments:".format(argc))
        for i in range(1, argc):
            print("{:d}: {}".format(i, argv[i]))
        print("{:d}: {}".format(argc, argv[argc]))
