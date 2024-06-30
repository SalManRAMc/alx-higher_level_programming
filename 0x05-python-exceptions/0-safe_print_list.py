#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print(my_list[i], end="")
            i += 1
        print("\n")
    except (IndexError):
        print("")
    return (i)
