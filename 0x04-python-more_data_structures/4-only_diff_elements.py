#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    res = set()
    for item in set_1:
        for element in set_2:
            if element != item:
                res.add(element)
                res.add(item)
            else:
                res.remove(element)
    return res
