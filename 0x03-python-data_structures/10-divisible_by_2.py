#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list_by2 = []
    for i in my_list:
        if i % 2 == 0:
            my_list_by2.append(True)
        else:
            my_list_by2.append(False)
    return (my_list_by2)
