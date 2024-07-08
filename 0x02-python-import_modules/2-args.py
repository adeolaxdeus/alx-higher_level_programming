#!/usr/bin/python3
import sys


def main():
    i = len(sys.argv)
    if i > 1:
        if (i - 1) == 1:
            arguments = "argument"
        else:
            arguments = "arguments"
        print("{} {}:".format((i - 1), arguments))
        for index in range(1, i):
            print("{}: {}".format(index, sys.argv[index]))
    else:
        print("0 arguments.")


if __name__ == "__main__":
    main()
