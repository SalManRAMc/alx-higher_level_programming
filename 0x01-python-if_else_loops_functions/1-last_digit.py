#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number % 10 == 0:
    lastdigit = 0
elif number >= 0:
    lastdigit = number % 10
else:
    lastdigit = -(10 - (number % 10))

print("Last digit of", number, "is", lastdigit, end=" ")

if lastdigit > 5:
    print("and is greater than 5")
elif lastdigit < 6 and lastdigit != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
