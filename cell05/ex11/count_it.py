#!/usr/bin/env python3

import sys

count = len(sys.argv) - 1

if count == 0:
    print("none")
else:
    print(f"parameters: {count}")
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
