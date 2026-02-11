#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    count = sys.argv[2].count(sys.argv[1])
    if count:
        print(count)
    else:
        print("none")
else:
    print("none")