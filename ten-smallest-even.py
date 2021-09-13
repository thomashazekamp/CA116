#!/usr/bin/env python3

n = 10
smalleste = int(input())

i = 0
while i < n - 1:
  v = int(input())
  if smalleste > v and v % 2 == 0:
    smalleste = v
  i = i + 1

print (smalleste)
