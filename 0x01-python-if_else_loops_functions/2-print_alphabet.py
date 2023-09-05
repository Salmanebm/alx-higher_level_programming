#!/usr/bin/python3
start = ord('a')
end = ord('z') + 1
alphabet = ""
for letter_dec in range(start, end):
    letter = chr(letter_dec)
    alphabet += letter
print(alphabet)
