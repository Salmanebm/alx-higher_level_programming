#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in my_list:
        i += 1
    i -= 1
    for j in my_list:
        print("{:d}".format(i))
        i -= 1
