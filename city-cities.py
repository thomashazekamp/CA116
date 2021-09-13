#!/usr/bin/env python3

s = input()
while s != "end":
   i = 0
   while i < len(s) and (s[i] != ","):
      i = i + 1
      if s[i] == "," and s[i - 4:i] == "City" and s[:4] != "City":
         print (s[:i])
   s = input()
