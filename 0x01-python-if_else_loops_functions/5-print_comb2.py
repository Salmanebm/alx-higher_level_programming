#!/usr/bin/python3
zero = 0
for num in range(100):
    if num < 10:
            print(f"0{num}, ", end="")
    else:
            print(f"{num}, ", end="")
