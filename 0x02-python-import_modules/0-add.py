#!/usr/bin/python3
import sys
from add_0 import add


def addition():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)), end="\n")


if __name__ == "__main__":
    import sys
    addition()