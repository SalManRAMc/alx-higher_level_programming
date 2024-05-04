#!/usr/bin/python3

"""
  This is a power function
"""
def pow(a, b):
    result = 1
    if b < 0:
        return (1 / pow(a, -b))  # Handle negative powers
    elif b == 0:
        return (1)
    else:
        for i in range(b):
            result *= a
        return result
