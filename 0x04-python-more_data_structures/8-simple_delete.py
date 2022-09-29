#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k, v in sorted(a_dictionary.items()):
        if(key == k):
            del a_dictionary[key]
    return a_dictionary
