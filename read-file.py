#!/usr/bin/env python3

with open("input.txt") as f:
   lines = f.readlines()

i = 0
while i < len(lines):
   lines[i] = lines[i].strip("\n")
   print (lines[i])
   i = i + 1
