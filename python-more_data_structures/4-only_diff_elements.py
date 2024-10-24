#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for s in (set_1, set_2):
        for element in s:
            new_set.add(element)
    return new_set
