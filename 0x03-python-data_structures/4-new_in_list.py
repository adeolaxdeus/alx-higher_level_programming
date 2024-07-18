#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if my_list is None or idx is None or element is None:
        return None
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    new_list = my_list[:]
    for num in range(len(new_list)):
        if num == idx:
            new_list[idx] = element
    return new_list
