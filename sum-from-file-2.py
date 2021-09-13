#!/usr/bin/env python3

import sys
file = sys.argv[1]
with open(file) as f:
   lines = f.readlines()

i = 0
total = 0
while i < len(lines):
   lines[i] = lines[i].rstrip()
   total = total + int(lines[i])
   i = i + 1
print (total)
