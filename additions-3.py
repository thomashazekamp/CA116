#!/usr/bin/env python3

i = 0
total_num = 0
while total_num != 1000:
   s = input()
   while i < len(s) and (s[i] != "+"):
      i = i + 1
   if i < len(s):
      total_num = int(s[0:i]) + int(s[(i + 1):len(s)])
      i = 0
   print (total_num)
