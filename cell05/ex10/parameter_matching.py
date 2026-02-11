#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    if (sys.argv[1] == input("What was the parameter? ")):
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")