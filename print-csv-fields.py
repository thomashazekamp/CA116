#!/usr/bin/env python3

a = []
s = input()
while s != "end":
   a.append(s)
   s = input()
n = int(input())

i = 0
while i < len(a):
   tokens = a[i].split(",")
   print (tokens[n])
   i = i + 1
