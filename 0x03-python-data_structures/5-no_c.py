#!/usr/bin/python3


def no_c(my_string):
    if my_string is None:
        return None
    new_string = ""
    for character in my_string:
        if character != "c" and character != "C":
            new_string += character
    return new_string
