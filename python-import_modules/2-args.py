#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    print(len(sys.argv) "arguments")
    for i in range(1, len(sys.argv)):
        print(i"." sys.argv[i])
