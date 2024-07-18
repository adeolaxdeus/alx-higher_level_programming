#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for row in matrix:
        for x in row:
            if x is row[-1]:
                print("{:d}".format(x))
            else:
                print("{:d}".format(x), end=" ")
