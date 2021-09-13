#!/usr/bin/env python3

a = [1, 2, 3, 4, 5]

p = len(a) - 1
i = 0
while i < len(a)/2:
  tmp = a[p]
  a[p] = a[i]
  a[i] = tmp
  p = p - 1
  i = i + 1
print (a)
