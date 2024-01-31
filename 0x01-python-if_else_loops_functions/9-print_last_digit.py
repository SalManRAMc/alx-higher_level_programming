#!/usr/bin/python3

def print_last_digit(number):
    i = 0

    if number < 0:
        i = 10 - (number % 10)
        print(i, end="")
        return (i)
    else:
        i = number % 10
        print(i, end="")
        return (i)
