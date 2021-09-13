#!/usr/bin/env python3

n = int(input())
x = 1
y = 0
i = 0
while i < n:
  if x < y:
    print (x)
    x = x + y
  else:
    print (y)
    y = y + x
  i = i + 1
