#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for item in range(len(my_list)):
        print("{}".format(int(my_list[item])))

if __name__ == "__main__":
    print_list_integer()