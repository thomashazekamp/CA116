#!/usr/bin/env python3

s = input()
m = len(s)
t = ""
i = 0
while i < m:
   if s[i] == " ":
      t = t
   else:
      t = t + s[i]
   i = i + 1
print (t)
