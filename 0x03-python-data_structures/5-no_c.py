#!/usr/bin/python3
def no_c(my_string):
    txt = ''
    for index in range(len(my_string)):
        if(my_string[index] == 'c'):
            continue
        elif(my_string[index] == 'C'):
            continue
        else:
            txt += my_string[index]
    return txt
