#!/usr/bin/python3


def no_c(my_string):
    for char in my_string:
        if char in ("c", "C"):
            continue
        else:
            print(char, end="")