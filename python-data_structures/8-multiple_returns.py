#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        new_tuple = (len(sentence), sentence[0])
    else:
        new_tuple = (0, None)
    return new_tuple
