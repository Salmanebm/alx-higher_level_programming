#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    char = chr(i)
    if char.islower():
        print(char, end='')
    else:
        print(char.lower(), end='')
print()
