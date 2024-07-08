#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv)
    if length > 1:
        print("{} arguments:".format(length - 1))
        for index in range(1, length):
            print("{}: {}".format(index, sys.argv[index]))
    else:
        print("0 arguments.")


if __name__ == "__main__":
    main()
