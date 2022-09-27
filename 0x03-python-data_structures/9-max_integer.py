#!/usr/bin/python3
def max_integer(my_list=[]):
    large = my_list[0]
    if(len(my_list) < 1):
        return None
    else:
        for item in my_list:
            if(item > large):
                large = item
        return large
