#!/usr/bin/python3
import sys


def main():
    result = 0
    length = len(sys.argv)
    if length < 1:
        print("0")
    else:
        for index in range(1, length):
            result += int(sys.argv[index])
        print(result)


if __name__ == "__main__":
    main()
