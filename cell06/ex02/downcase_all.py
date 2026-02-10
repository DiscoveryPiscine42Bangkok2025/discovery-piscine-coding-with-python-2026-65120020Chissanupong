#!/usr/bin/env python3

import sys

def downcase_it(text):
    return text.lower()

params = len(sys.argv)

if params < 2:
    print("none")
else:
    for i in range(1, params):
        print(downcase_it(sys.argv[i]))
