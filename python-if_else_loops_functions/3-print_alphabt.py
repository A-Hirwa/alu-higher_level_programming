#!/usr/bin/python3
for i in range(97,123):
    if chr(i) in ("e", "q"):
        continue
    else:
        print("{}".format(chr(i)), end="")
