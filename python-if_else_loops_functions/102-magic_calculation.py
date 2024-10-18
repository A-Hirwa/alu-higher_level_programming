#!/usr/bin/python3
def magic_calculation(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")
    if a < b:
        print("Returning c")
        return c
    elif b > c:
        print("Returning a + b")
        return a + b
    else:
        print("Returning (a * b) - c")
        return (a * b) - c
