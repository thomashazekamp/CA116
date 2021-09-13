#!/usr/bin/env python3

import sys

file = sys.argv[1]

with open(file) as f:
   all_lines = f.read().split()

i = 0
total = 0
while i < len(all_lines):
   total = total + int(all_lines[i])
   i = i + 1

print (total)
