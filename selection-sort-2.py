#!/usr/bin/env python3

a = []
s = input()
while s != "end":
   a.append(s)
   s = input()
i = input()
p = int(i)
j = int(i) + 1
while j < len(a):
   if int(a[j]) < int(a[p]):
      p = j
   j = j + 1
print (p)
