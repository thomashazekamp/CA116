#!/usr/bin/env python3

import sys

target = sys.argv[1]

s = input()
i = 0
comma = 0

while i < len(s) - 1:
   if s[i] == ",":
      comma = comma + 1
   if s[i:i + len(target)] == target:
      print (comma)
   i = i + 1
