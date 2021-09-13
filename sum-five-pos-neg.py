#!/usr/bin/env python3

n = 5

total_positive = 0
total_negative = 0
i = 0
while i < n:
   m = int(input())
   if m < 0:
      total_negative = total_negative + m
   else:
      total_positive = total_positive + m
   i = i + 1

print (total_negative, total_positive)
