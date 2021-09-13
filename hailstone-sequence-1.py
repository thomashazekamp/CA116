#!/usr/bin/env python3

x = int(input())
y = int(input())

z = y

i = 0
print (y)
while i < x - 1:
   if z % 2 == 0:
      m = (z // 2)
      print (m)
      z = m
      i = i + 1
   else:
      m = ((3 * z) + 1)
      print (m)
      z = m
      i = i + 1
