#!/usr/bin/env python3

s = input()
i = 0
while i < len(s) and (s[i] < "0" or "9" < s[i]):
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
      j = j + 1

   while j < len(s) and (s[j] < "0" or "9" < s[j]):
      j = j + 1

   if j < len(s):
      p = j
      while p < len(s) and ("0" <= s[p] and s[p] <= "9"):
         p = p + 1
      print (s[j:p], len(s[:j]))
