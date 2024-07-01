#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0
    """
        Prints the result of a division
    """
    try:
        result = a / float(b)
    except (ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)