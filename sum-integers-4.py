#!/usr/bin/env python3

import sys

file_names = sys.argv[1:]
final_total = 0

i = 0
while i < len(file_names):
   file = file_names[i]
   with open(file) as f:
      all_lines = f.read().split()

   j = 0
   total = 0
   while j < len(all_lines):
      total = total + int(all_lines[j])
      j = j + 1
   final_total = final_total + total
   i = i + 1
print (final_total)
