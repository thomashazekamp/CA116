#!/usr/bin/env python3

n = 10
j = 0
while j < n:
   s = input()
   j = j + 1
   i = 0
   while i < len(s) and (s[i] != "+"):
      i = i + 1
   if i < len(s):
      total_num = int(s[0:i]) + int(s[(i + 1):len(s)])
   print (total_num)
