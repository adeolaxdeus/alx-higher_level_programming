#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if a_dictionary != {}:
        max_key = None
        max_value = 0
        for key, value in a_dictionary.items():
            if max_value < value:
                max_value = value
                max_key = key
        return max_key
