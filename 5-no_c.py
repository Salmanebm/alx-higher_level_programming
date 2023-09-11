#!/usr/bin/python3
def no_c(my_string):
    alt = ""
    for c in my_string:
        if c == 'c' or c == 'C':
            alt += " "
        else:
            alt += c
    return (alt)