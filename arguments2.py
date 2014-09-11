#!/usr/bin/python
import sys
final = 0

for arg in sys.argv:
    if  arg.isdigit():
        final += int(arg)

print final
