#!/usr/bin/python3

def uppercase(str):
    i = 0
    while i < len(str):
            print("{:s}".format(chr(ord(str[i]) - 32)), end="")
        i += 1
    print("")
