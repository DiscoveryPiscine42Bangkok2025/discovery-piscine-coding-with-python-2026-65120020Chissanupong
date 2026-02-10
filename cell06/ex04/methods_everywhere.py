#!/usr/bin/env python3

import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + "Z" * (8 - len(text)))

params = len(sys.argv)

if params < 2:
    print("none")
else:
    for i in range(1, params):
        word = sys.argv[i]
        if len(word) > 8:
            shrink(word)
        elif len(word) < 8:
            enlarge(word)
        else:
            print(word)
