#!/usr/bin/env python

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print
print txt.read()
