#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for item in my_list:
        txt = str(item).format()
        print("{}".format(txt), end="\n")
