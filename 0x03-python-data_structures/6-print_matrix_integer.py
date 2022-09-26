#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if(len(matrix[0]) < 1):
        print("", end="\n")
    else:
        for object in matrix:
            for index in range(len(object)):
                if(index < (len(object) - 1)):
                    print("{:d} ".format(object[index]), end="")
                else:
                    print("{:d}".format(object[index]), end="\n")
