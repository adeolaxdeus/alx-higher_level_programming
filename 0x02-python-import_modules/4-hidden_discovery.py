#!/usr/bin/python3
import hidden_4.pyc


def main():
    for name in dir(hidden_4.pyc):
        if not name.startswith('__'):
            print(name)


if _name__ == "__main__":
    main()
