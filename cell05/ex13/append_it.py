#!/usr/bin/env python3

import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    found = False

    for word in params:
        if not word.endswith("ism"):
            print(word + "ism")
            found = True

    if not found:
        print("none")
