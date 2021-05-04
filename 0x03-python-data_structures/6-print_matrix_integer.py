#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        len_x = len(matrix[0])
        len_y = (len(matrix))
        for y in range(len_y):
            for x in range(len_x):
                print("{:d}".format(matrix[y][x]), end='')
                if x != (len_x - 1):
                    print(" ", end='')
                else:
                    print()
    else:
        print("faf")
