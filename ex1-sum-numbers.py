#!/usr/bin/env python3

n = int(input())

total = 0
i = 0
while i < n:
   m = input()
   if m == ("one"):
      total = total + 1
   elif m == ("two"):
      total = total + 2
   elif m == ("three"):
      total = total + 3
   elif m == ("four"):
      total = total + 4
   elif m == ("five"):
      total = total + 5
   i = i + 1

print (total)
