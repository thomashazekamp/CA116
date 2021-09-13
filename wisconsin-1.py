#!/usr/bin/env python3

s = input()
while s != "end":
   i = 0
   num_commas = 0
   while num_commas < 2 or i >= len(s):
      if s[i] == ",":
         num_commas = num_commas + 1
      if s[i] == "W" and s[i + 1] == "I":
         print (s[:i - 1])
      i = i + 1
   s = input()
