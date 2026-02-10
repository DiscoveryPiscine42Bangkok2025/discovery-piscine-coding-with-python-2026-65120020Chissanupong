#!/usr/bin/env python3

print("Enter a number: ")
number = int(input())

i = 0
while i < 10:
    result = number * i
    print(f"{i} x {number} = {result}")
    i += 1
