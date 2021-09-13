#!/usr/bin/env python3

s = input()
while s != "end":
   i = 0
   while i < len(s) and (s[i] != ":"):
      i = i + 1
   if i < len(s):
      first_word = s[:i]
   j = 1
   p = len(s) - 1
   while j < len(s) and (s[p] != ":"):
      p = len(s) - j
      j = j + 1
   if j < len(s):
      p = p + 1
      usr_command = s[p:]
   print (first_word, usr_command)
   s = input()
