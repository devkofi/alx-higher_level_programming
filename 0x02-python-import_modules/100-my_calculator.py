#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def mathematics():
    arguments = len(sys.argv) - 1
    operators = "+-*/"
    if(arguments < 3 or arguments > 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>".
              format(), end="\n")
        exit(1)
    else:
        for operator in operators:
            if(sys.argv[2] != operator):
                continue
                print("Unknown operator. Available operators: +, -, * and /".
                      format(), end="\n")
                exit(1)
            else:
                if(sys.argv[2] == "+"):
                    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                          sys.argv[3], int(sys.argv[1]) + int(sys.argv[3])),
                          end="\n")
                elif(sys.argv[2] == "-"):
                    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                          sys.argv[3], int(sys.argv[1]) - int(sys.argv[3])),
                          end="\n")
                elif(sys.argv[2] == "*"):
                    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                          sys.argv[3], int(sys.argv[1]) * int(sys.argv[3])),
                          end="\n")
                else:
                    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2],
                          sys.argv[3], int(sys.argv[1]) / int(sys.argv[3])),
                          end="\n")


if __name__ == "__main__":
    mathematics()
