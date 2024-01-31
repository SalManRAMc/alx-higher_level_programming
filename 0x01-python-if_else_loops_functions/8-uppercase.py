#!/usr/bin/python3

def uppercase(str):
    i = 0
    while i < len(str):
        if str[i] == " ":
            print(" ")
        else:
            print("{:c}".format(chr(ord(str[i]) - 32)))
        i += 1
