#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
if int(number[len(number)-1]) > 5:
    print("Last digit of ", number, " is ",number[len(number)-1], "and is greater than 5")
elif int(number[len(number)-1]) == 0:
    print("Last digit of ", number, " is ",number[len(number)-1],"is zero")
elif int(number[len(number)-1]) < 6 and not 0:
    print("Last digit of ", number, " is ",number[len(number)-1],"is less than 6 and not 0")
