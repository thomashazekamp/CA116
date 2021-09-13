#!/usr/bin/env python3

import sys

first_input = sys.stdin.readlines()

i = 0
while i < len(first_input):
   p = first_input[i].split("/")
   n = p[len(p) - 1]
   last = n.rstrip()
   i = i + 1
   print (last)
