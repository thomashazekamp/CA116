#!/usr/bin/env python3

total_positive = 0
total_negative = 0

n = int(input())
while n != 0:
   if n < 0:
      total_negative = total_negative + n
   else:
      total_positive = total_positive + n
   n = int(input())

print (total_negative, total_positive)
