#!/usr/bin/python3
start = ord('a')
end = ord('z') + 1
alphabet = ''.join(chr(letter_code) for letter_code in range(start, end))
print(alphabet)
