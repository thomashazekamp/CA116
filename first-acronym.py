#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and (s[i] < "A" or s[i] > "Z"):
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and (s[j] >= "A" and s[j] <= "Z"):
      j = j + 1
   print (s[i:j], len(s[:i]))
