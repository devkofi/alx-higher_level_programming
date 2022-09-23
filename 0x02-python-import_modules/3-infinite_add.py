#!/usr/bin/python3
import sys


def print_arguments():
    counter = 0
    arguments = len(sys.argv)-1
    if(arguments < 1):
        print("{}".format(counter))
    else:
        for arg in range(1, arguments + 1):
            counter += int(sys.argv[arg])
        print("{}".format(counter))


if __name__ == "__main__":
    print_arguments()
