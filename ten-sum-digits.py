#!/usr/bin/env python3

n = 10

total = 0
i = 0
while i < n:
  num = int(input())
  if num * -1 > 0:
    num = num * -1
  else:
    num = num
  lastd = num % 10
  total = total + lastd
  i = i + 1

print (total)
