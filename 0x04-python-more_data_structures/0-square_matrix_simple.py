#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    test = []
    for i in matrix:
        test.append(list(map(lambda x: (x*x) , i)))
    return (test)
