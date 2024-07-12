#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    a = 0
    for key in a_dictionary:
        if a < a_dictionary[key]:
            a = a_dictionary[key]
            b = key
    return b
