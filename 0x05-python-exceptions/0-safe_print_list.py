#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    realnumbers = 0
    i = 0
    try:
        while i is not x:
            print(my_list[i], end="")
            realnumbers += 1
            i += 1
        print("\n")
        return (realnumbers)
    except (IndexError):
        print("")
