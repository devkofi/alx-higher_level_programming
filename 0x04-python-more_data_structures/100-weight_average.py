#!/usr/bin/python3


def weight_average(my_list=[]):
    if(len(my_list) > 0):
        numerator = 0
        denominator = 0
        for item in my_list:
            numerator += item[0] * item[(len(item) - 1)]
            denominator += item[(len(item) - 1)]
        return (numerator/denominator)
    else:
        return 0
