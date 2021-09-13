#!/usr/bin/env python3

s = input()
while s != "end":
   if s[len(s) - 1] == "t":
      s = input()
   else:
      i = 1
      p = len(s) - 1
      while i < len(s) and s[p] != "/":
         p = len(s) - i
         i = i + 1
      if s[p] == "/":
         print (s[p + 1:])
      s = input()
