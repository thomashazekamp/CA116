#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
seen = {}

i = 0
while i < len(lines):
   line = lines[i]
   line = line.rstrip()
   j = len(line) - 1
   while line[j] != ".":
      j = j - 1
   seen[line[:j]] = line[j + 1:]
   i = i + 1

for key, value in seen.items():
   if value == "correct":
      print (key)
