#!/usr/bin/env python3

import sys

count = len(sys.argv) - 1

if count < 2:
    print("none")
else:
    i = len(sys.argv) - 1
    while i >= 1:
        print(sys.argv[i])
        i -= 1
