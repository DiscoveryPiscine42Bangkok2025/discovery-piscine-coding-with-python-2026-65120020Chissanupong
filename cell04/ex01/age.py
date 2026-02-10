#!/usr/bin/env python3

age = int(input("Please tell me your age: "))

years = 0

print(f"You are currently {age} years old.")

while years < 30:
    years += 10
    print(f"In {years} years, you'll be {age + years} years old.")
