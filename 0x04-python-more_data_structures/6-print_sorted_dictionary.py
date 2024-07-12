#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    my_keys = sorted(a_dictionary)
    for keys in my_keys:
        print("{}: {}".format(keys, a_dictionary[keys]))
