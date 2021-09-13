#!/usr/bin/env python3

import sys

tot_argvs = sys.argv[1:]
final_total = 0
i = 0
while i < len(tot_argvs):
   file = tot_argvs[i]
   with open(file) as f:
      lines = f.readlines()

   j = 0
   total = 0
   while j < len(lines):
      lines[j] = lines[j].rstrip()
      total = total + int(lines[j])
      j = j + 1
   final_total = final_total + total
   i = i + 1
print (final_total)
