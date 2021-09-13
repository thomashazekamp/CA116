#!/usr/bin/env python3

s = input()
total = 0
while s != "end":
   i = 1
   p = len(s) - 1
   while i < len(s) and s[p] != "y":
      p = len(s) - i
      i = i + 1
   if s[p + 2:] == "correct":
      total = total + 1
   s = input()
print (total)
