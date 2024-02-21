#!/usr/bin/python3
def no_c(my_string):
    stringnew = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            stringnew += my_string[i]
    return stringnew