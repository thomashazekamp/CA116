#!/usr/bin/env python3

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

s = input()
while s != "end":
   t = ""
   i = 0
   while i < len(s):
      if "A" <= s[i] and s[i] <= "Z":
         j = 0
         while s[i] != upper[j]:
            j = j + 1
         t = t + lower[j]
      else:
         t = t + s[i]
      i = i + 1
   print (t)
   s = input()
