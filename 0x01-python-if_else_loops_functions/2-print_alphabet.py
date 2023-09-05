#!/usr/bin/python3
start = ord('a')
end = ord('z') + 1
for letter_dec in range(start, end):
    letter = chr(letter_dec)
    print("{}".format(letter))
