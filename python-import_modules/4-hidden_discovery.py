#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    functions = dir(hidden_4)
    functions.sort()
    for func in functions:
        if func.startswith("__"):
            continue
        print(func)
