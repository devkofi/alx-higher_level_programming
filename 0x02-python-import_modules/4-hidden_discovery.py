#!/usr/bin/python3
import hidden_4


def print_magic_names():
    items = dir(hidden_4)
    length = len(items)
    for item in range(length):
        if("__" in items[item]):
            continue
        print("{}".format(items[item]), end="\n")


if __name__ == "__main__":
    import sys
    print_magic_names()
