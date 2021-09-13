#!/usr/bin/env python3

a = []
i = 0
while i < 3:
   s = int(input())
   a.append(s)
   i = i + 1

if a[0] <= a[1] and a[0] <= a[2]:
   print (a[0])
   if a[1] <= a[2]:
      print (a[1])
      print (a[2])
   else:
      print (a[2])
      print (a[1])

elif a[1] <= a[0] and a[1] <= a[2]:
   print (a[1])
   if a[0] <= a[2]:
      print (a[0])
      print (a[2])
   else:
      print (a[2])
      print (a[0])

elif a[2] <= a[0] and a[2] <= a[1]:
   print (a[2])
   if a[0] <= a[1]:
      print (a[0])
      print (a[1])
   else:
      print (a[1])
      print (a[0])
