#!/usr/bin/python3

def fizzbuzz():
    for i in (0, 101):
        if (i % 3 == 0):
            print("Fizz", end="")
        if (i % 5 == 0):
            print("Buzz", end="")
        print(" ")
