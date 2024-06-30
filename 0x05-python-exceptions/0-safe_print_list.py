#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    realnumbers = 0
    try:
        while i < x:
            print(my_list[i], end="")
            realnumbers += 1
    except:
        print("An Unknown exception has been raised")
