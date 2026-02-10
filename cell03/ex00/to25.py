#!/usr/bin/env python3

print("Enter a number less than 25")
number = int(input())

if number <= 25:
    i = number
    while i <= 25:
        print(f"Inside the loop, my variable is {i}")
        i += 1
else:
    print("Error")
