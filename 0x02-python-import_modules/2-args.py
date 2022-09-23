#!/usr/bin/python3
import sys


def print_arguments():
    arguments = len(sys.argv)-1
    if(arguments < 1):
        print("{} arguments.".format(arguments))
    elif(arguments == 1):
        print("{} argument:".format(arguments))
        print("{}: {}".format(arguments, sys.argv[arguments]))
    else:
        print("{} arguments:".format(arguments))
        for arg in range(1, arguments + 1):
            print("{}: {}".format(arg, sys.argv[arg]))


if __name__ == "__main__":
    print_arguments()
