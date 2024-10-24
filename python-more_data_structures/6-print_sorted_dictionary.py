#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dictionary = {}
    sorty = sorted(a_dictionary)
    for key in sorty:
        new_dictionary[key] = a_dictionary[key]
    return new_dictionary
