#!/usr/bin/python3
def best_score(a_dictionary):
    high = 0
    score = ""
    if(a_dictionary != None):
        for k, v in sorted(a_dictionary.items()):
            if(v > high):
                score = k
        return score
    else:
        return None
