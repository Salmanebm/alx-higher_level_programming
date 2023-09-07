#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0")
    elif count == 1:
        print("enter the second number")
    else:
        res = 0
        for i in range(count):
            res += int(sys.argv[i + 1])
        print("{}".format(res))
