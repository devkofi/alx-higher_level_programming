#!/usr/bin/python3
def common_elements(set_1, set_2):
    res = set()
    for item in set_1:
        for element in set_2:
            if element != item:
                continue
            else:
                res.add(element)
    return res
