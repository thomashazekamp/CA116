#!/usr/bin/env python3

n = 10
smallest = int(input())

i = 0
while i < n - 1:
  v = int(input())
  if smallest > v:
    smallest = v
  i = i + 1

print (smallest)
