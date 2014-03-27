#!/usr/bin/env python

def count(x, y):
  y = y + 1
  print "\n"

  for i in range(x, y):
    print i

print "What number would you like to count from?"
x1 = raw_input()
print "What number would you like to count to?"
y1 = raw_input()

x1 = int(x1)
y1 = int(y1)

count(x1, y1)
