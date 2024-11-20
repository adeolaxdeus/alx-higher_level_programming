#!/usr/bin/env bash
def uppercase(str):
    string = ""
    for char in str:
        if ('a' <= char <= 'z'):
            string += chr(ord(char) - 32)
        else:
            string += char
    print(string)
