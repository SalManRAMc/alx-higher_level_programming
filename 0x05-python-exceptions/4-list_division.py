#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_index = 0
    indexresult = 0
    newlist = list()
    while list_index < list_length:
        try:
            indexresult = my_list_1[list_index] / my_list_2[list_index]
            newlist.append(indexresult)
        except (TypeError, ValueError):
            print("wrong type")
            newlist.append(0)
        except ZeroDivisionError:
            print("division by 0")
            newlist.append(0)
        except IndexError:
            print("out of range")
            newlist.append(0)
        finally:
            list_index += 1
    return (newlist)
