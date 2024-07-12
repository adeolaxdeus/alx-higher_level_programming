#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    update = {k: (value if k == key else v) for k, v in a_dictionary.items()}
    # add key if not present
    if key not in update:
        update[key] = value
    return update
