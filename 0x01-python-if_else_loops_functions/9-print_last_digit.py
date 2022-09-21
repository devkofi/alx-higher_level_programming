#!/usr/bin/python3
def print_last_digit(number):
    num = str(abs(number))
    last_digit = num[-1]
    print("{}".format(last_digit), end="")
    return last_digit
