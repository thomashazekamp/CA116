#!/usr/bin/env python3

p = 5
n = int(input())
previous = n

i = 0
while i < p:
   m = int(input())
   if m > previous:
      previous = m
      print ("higher")
   elif m < previous:
      previous = m
      print ("lower")
   elif m == previous:
      previous = m
      print ("equal")
   i = i + 1
