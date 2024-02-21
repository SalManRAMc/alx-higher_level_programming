#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(my_list[i]), "\n") 
        #remember that in order to print something as a specific data type
        #you have to specify the data type inside the curly braces