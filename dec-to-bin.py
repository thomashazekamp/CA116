#!/usr/bin/env python3

s = input()

i = 0
while i < len(s):
   if int(s) % 2 != 0:
      final = int(s) / (2 ** i)
   i = i + 1

print (final)
