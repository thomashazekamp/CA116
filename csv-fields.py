#!/usr/bin/env python3

s = input()
word = 0
i = 0
while word < 11:
   start = i
   while i < len(s) and (s[i] != ","):
      i = i + 1
   if i <= len(s):
      print (s[start:i])
   i = i + 1
   word = word + 1
