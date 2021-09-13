#!/usr/bin/env python3

a = []
s = ""
while s != "end":
  s = input()
  i = 0
  no = 0
  while i < len(a):
    if s != a[i]:
      i = i + 1
    elif s == a[i]:
      i = len(a)
      no = 1
  if no == 1 or s == "end":
    no = 0
  else:
    a.append(s)

i = 0
while i < len(a):
  print(a[i])
  i = i + 1
