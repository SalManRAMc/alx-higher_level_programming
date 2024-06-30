#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    realnumbers = 0
    while i != x:
        try:
            print("{:d}".format(my_list[i]), end="")
            realnumbers += 1
        except (TypeError, ValueError):
            pass
        finally:
            i += 1
    print()
    return (realnumbers)


