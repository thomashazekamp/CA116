#!/usr/bin/env python3

a = []
m = input()
while m != "end":
   a.append(int(m))
   m = input()
i = 0
n = int(input())
while i < len(a):
   print (a[i] + n)
   i = i + 1
