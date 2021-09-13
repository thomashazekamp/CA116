#!/usr/bin/env python3

s = input()

number = 0
i = 0
total = 0
while number < 5:
   start = i
   while i < len(s) and (s[i] != "+"):
      i = i + 1
   num = (s[start:i])
   total = total + int(num)
   i = i + 1
   number = number + 1
print (total)
