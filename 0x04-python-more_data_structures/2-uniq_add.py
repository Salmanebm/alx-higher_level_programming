#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    new_list = set()
    for i in my_list:
        new_list.add(i)
    res = reduce(lambda a, b: a + b, new_list)
    return (res)
