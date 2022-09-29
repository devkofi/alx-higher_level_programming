#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # new_list = []
    # for item in my_list:
    #     if(item==search):
    #         item = map(lambda x: replace)
    return list(map(lambda a: replace if (a == search) else a, my_list))
