#!/usr/bin/env python3

a = []

s = input()
while s != "end":
   a.append(s)
   s = input()
w = input()
while w != "end":
   a.append(w)
   w = input()

i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if int(a[j]) < int(a[p]):
         p = j
      j = j + 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   i = i + 1
   print (tmp)
