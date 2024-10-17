#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if 123 > ord(ch) > 96:
            char = chr(ord(ch)-32)
        print("{}".format(ch), end="")
    print("")
