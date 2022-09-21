#!/usr/bin/python3
def remove_char_at(str, n):
    if(n >= 0):
        txt = str[:n] + str[n+1:]
    else:
        txt = str[:]
    return txt
