#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    if sys.argv[1].count("z"):
        print("z" * sys.argv[1].count("z"))
    else:
        print("none")
else:
    print("none")