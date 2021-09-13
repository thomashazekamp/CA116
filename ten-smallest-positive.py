#!/usr/bin/env python3

n = 10
smallestp = int(input())

i = 0
while i < n - 1:
  v = int(input())
  if smallestp > v and v > 0:
    smallestp = v
  i = i + 1
print (smallestp)
