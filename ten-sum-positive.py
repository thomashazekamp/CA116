#!/usr/bin/env python3

n = 10
total = 0

i = 0
while i < 10:
  n = int(input())
  if n > 0:
    total = total + n
  else:
    total = total + 0
  i = i + 1

print (total)