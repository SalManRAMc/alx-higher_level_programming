#!/usr/bin/python3

def uppercase(str):
    i = 0
    while (str[i] != "\0"):
        if (str[i] == " "):
            print(" ")
        else:
            print("{:c}".format(ord(i) + 32))
