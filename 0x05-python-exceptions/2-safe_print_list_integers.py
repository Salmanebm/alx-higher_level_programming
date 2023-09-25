#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    red = 0
    i = 0
    for i in range(x):
        try:
            print("{}".format(my_list[0]), end="")
            red += 1
        except (IndexError, TypeError):
            break
    print("")
    return (red)