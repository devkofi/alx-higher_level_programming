#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    item = ''
    if(len(sentence) > 0):
        for word in sentence:
            for index in range(len(word)):
                count += 1
        this_tuple = (count, sentence[0])
        return this_tuple
    else:
        return None
