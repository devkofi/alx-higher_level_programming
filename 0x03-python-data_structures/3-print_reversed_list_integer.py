#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    for item in range(len(new_list)):
        print("{:d}".format(new_list[item]))
