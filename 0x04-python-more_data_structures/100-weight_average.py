#!/usr/bin/python3
from functools import reduce


def weight_average(my_list=[]):
    if(len(my_list) > 0):
        numerator = 0
        denominator = 0
        for item in my_list:
            numerator += reduce(lambda x, y: x*y, item)
            denominator += reduce(lambda x, y: y, item)
        return (numerator/denominator)
    else:
        return 0
