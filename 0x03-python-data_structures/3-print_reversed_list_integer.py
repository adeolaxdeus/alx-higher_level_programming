#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    length = len(my_list) - 1
    for index in range(length, -1, -1):
        print("{:d}".format(my_list[index]))