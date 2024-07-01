#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0
    """
        Prints the result of a division
    """
    try:
        result = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
